terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.4"
    }
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Project     = "FarmwiseAI-Task5"
      Team        = var.team_prefix
      Environment = var.environment
      ManagedBy   = "Terraform"
      City        = "Coimbatore"
      Ward        = "29"
    }
  }
}

# 1. Core Service: S3 Storage Bucket
resource "aws_s3_bucket" "urban_data" {
  bucket        = "${var.team_prefix}-urban-data-mumbai"
  force_destroy = false
}

resource "aws_s3_bucket_versioning" "urban_versioning" {
  bucket = aws_s3_bucket.urban_data.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "urban_encryption" {
  bucket = aws_s3_bucket.urban_data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "urban_pab" {
  bucket                  = aws_s3_bucket.urban_data.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_cors_configuration" "urban_cors" {
  bucket = aws_s3_bucket.urban_data.id
  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD", "PUT", "POST"]
    allowed_origins = ["*"]
    max_age_seconds = 3600
  }
}

# 2. Core Service: Amazon DynamoDB NoSQL Tables
resource "aws_dynamodb_table" "urban_assets" {
  name         = "${var.team_prefix}-urban-assets"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "Asset_ID"
  range_key    = "Street_ID"

  attribute {
    name = "Asset_ID"
    type = "S"
  }
  attribute {
    name = "Street_ID"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }
}

resource "aws_dynamodb_table" "work_orders" {
  name         = "${var.team_prefix}-work-orders"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "Work_Order_ID"
  range_key    = "Priority_Level"

  attribute {
    name = "Work_Order_ID"
    type = "S"
  }
  attribute {
    name = "Priority_Level"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }
}

# 3. Core Service: AWS Lambda (Using Pre-Existing FAI-TCE-LambdaExecutionRole)
data "archive_file" "lambda_zip" {
  type        = "zip"
  output_path = "${path.module}/lambda.zip"
  source {
    content  = file("${path.module}/../lambda/lambda_function.py")
    filename = "lambda_function.py"
  }
}

resource "aws_lambda_function" "api_lambda" {
  function_name    = "${var.team_prefix}-urban-api"
  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime          = "python3.12"
  handler          = "lambda_function.lambda_handler"
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout
  # Referencing pre-existing role as per FarmwiseAI Access Guide rules:
  role             = "arn:aws:iam::387039786704:role/FAI-TCE-LambdaExecutionRole"

  environment {
    variables = {
      S3_BUCKET            = aws_s3_bucket.urban_data.id
      DYNAMO_ASSETS_TABLE  = aws_dynamodb_table.urban_assets.id
      DYNAMO_ORDERS_TABLE  = aws_dynamodb_table.work_orders.id
      APP_PREFIX           = var.team_prefix
      ENVIRONMENT          = var.environment
    }
  }
}

# 4. Core Service: Amazon API Gateway HTTP API (v2)
resource "aws_apigatewayv2_api" "http_api" {
  name          = "${var.team_prefix}-urban-gateway"
  protocol_type = "HTTP"

  cors_configuration {
    allow_origins = ["*"]
    allow_methods = ["GET", "POST", "OPTIONS"]
    allow_headers = ["Content-Type", "Authorization", "X-Api-Key"]
    max_age       = 3600
  }
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                 = aws_apigatewayv2_api.http_api.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.api_lambda.arn
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "detect" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "POST /api/v1/detect"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_route" "query" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "POST /api/v1/query"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_route" "work_orders" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "GET /api/v1/work-orders"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_route" "health" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "GET /health"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_stage" "stage" {
  api_id      = aws_apigatewayv2_api.http_api.id
  name        = var.environment
  auto_deploy = true
}

resource "aws_lambda_permission" "api_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.api_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.http_api.execution_arn}/*/*"
}
