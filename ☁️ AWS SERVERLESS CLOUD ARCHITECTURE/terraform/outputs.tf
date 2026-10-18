output "api_gateway_endpoint" {
  description = "Base URL of HTTP API Gateway"
  value       = "${aws_apigatewayv2_api.http_api.api_endpoint}/${var.environment}"
}

output "cloudfront_domain_name" {
  description = "CloudFront CDN domain name"
  value       = aws_cloudfront_distribution.cdn.domain_name
}

output "s3_bucket_name" {
  description = "S3 bucket for urban intelligence assets"
  value       = aws_s3_bucket.urban_data.id
}

output "lambda_arn" {
  description = "ARN of serverless AI lambda function"
  value       = aws_lambda_function.api_lambda.arn
}

output "iam_role_arn" {
  description = "IAM role ARN with least-privilege policies"
  value       = aws_iam_role.lambda_role.arn
}
