resource "aws_s3_bucket" "my-s3-bucket-vs1" {

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}