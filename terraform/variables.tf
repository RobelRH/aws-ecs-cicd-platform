variable "aws_region" {
  description = "AWS region used for the project"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "aws-ecs-cicd-platform"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "portfolio"
}