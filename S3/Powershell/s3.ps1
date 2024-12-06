Import-Module AWS.Tools.S3

$region = "us-east-1"


$bucketName = Read-Host -Prompt 'Enter the name off the bucket'

Write-Host "AWS Region: $region"
Write-Host "S3 Bucket: $bucketName"

New-S3Bucket -BucketName $bucketName -Region $region