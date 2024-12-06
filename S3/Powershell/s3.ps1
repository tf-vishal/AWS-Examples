Import-Module AWS.Tools.S3

$region = "us-east-1"


$bucketName = Read-Host -Prompt 'Enter the name off the bucket'

Write-Host "AWS Region: $region"
Write-Host "S3 Bucket: $bucketName"

function BucketExist{
    $bucket = Get-S3Bucket -BucketName $bucketName -ErrorAction SilentlyContinue
    return $null -ne $bucket
}

if (-not (BucketExist)) {
    <# Action to perform if the condition is true #>
    Write-Host "Bucket Does Not Exist"
    New-S3Bucket -BucketName $bucketName -Region $region
}else {
    <# Action when all if and elseif conditions are false #>
    Write-Host "Bucket already exist"
}

#create a new file

$fileName = "myfile.txt"
$fileContent = "Hello World!"
Set-Content -Path $fileName -Value $fileContent

Write-S3Object -BucketName $bucketName -File $fileName -Key $fileName -Region $region