variable "aws_region" {
  description = "AWS deployment region (Mumbai)"
  type        = string
  default     = "ap-south-1"
}

variable "team_prefix" {
  description = "Resource prefix for Team 24"
  type        = string
  default     = "fai-tce-team24"
}

variable "environment" {
  description = "Target deployment environment"
  type        = string
  default     = "prod"
}

variable "lambda_memory_size" {
  description = "Lambda memory allocation in MB"
  type        = number
  default     = 2048
}

variable "lambda_timeout" {
  description = "Lambda timeout in seconds"
  type        = number
  default     = 30
}
