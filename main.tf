terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.82.2" # Specify your desired version
    }
  }
}

provider "aws" {
  region  = "ap-south-1"   # Replace with your desired region
  profile = "default"     # Optional: Use if you're using AWS CLI profiles
}
resource "aws_lambda_function" "s3_rds_lambda" {
  function_name = "s3-rds-lambda"
  package_type  = "Image"
  image_uri     = "686255964404.dkr.ecr.ap-south-1.amazonaws.com/s3-rds-image:latest"

  role = aws_iam_role.lambda_role.arn
}

resource "aws_iam_role" "lambda_role" {
  name               = "lambda_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}
