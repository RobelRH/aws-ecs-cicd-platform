data "aws_iam_policy_document" "ecs_execution_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "ecs_execution" {
  name = "ecs-cicd-portfolio-execution-role"

  assume_role_policy = data.aws_iam_policy_document.ecs_execution_assume_role.json

  tags = {
    Name = "${var.project_name}-${var.environment}-execution-role"
  }
}

data "aws_iam_policy_document" "ecs_execution" {
  statement {
    sid    = "ECRAuthorization"
    effect = "Allow"

    actions = [
      "ecr:GetAuthorizationToken"
    ]

    resources = ["*"]
  }

  statement {
    sid    = "PullApplicationImage"
    effect = "Allow"

    actions = [
      "ecr:BatchCheckLayerAvailability",
      "ecr:GetDownloadUrlForLayer",
      "ecr:BatchGetImage"
    ]

    resources = [
      aws_ecr_repository.app.arn
    ]
  }

  statement {
    sid    = "WriteContainerLogs"
    effect = "Allow"

    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]

    resources = [
      "${aws_cloudwatch_log_group.ecs.arn}:*"
    ]
  }
}

resource "aws_iam_role_policy" "ecs_execution" {
  name = "ecs-cicd-portfolio-execution-policy"
  role = aws_iam_role.ecs_execution.id

  policy = data.aws_iam_policy_document.ecs_execution.json
}