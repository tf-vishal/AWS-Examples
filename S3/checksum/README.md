## Create New S3 Bucket

```md
aws s3 mb s3://checksums-example-vs1
```

## Create a file that we will do checksum on

```
echo "Hello Mars" > myfile.txt
```

## Get a checksum of a file or md5 
```
md5sum myfile.txt
```
# 8ed2d86f12620cdba4c976ff6651637f  myfile.txt'


## Upload our file to s3 and see the etag
```
aws s3 cp myfile.txt s3://checksums-example-vs1
aws s3api head-object --bucket checksums-example-vs1 --key myfile.txt
```

## Let's upload a file with different kinf of checksum

```sh
sudo apt install rhash -y
rhash --crc32 myfile.txt
```

```
aws s3api get-object \
--bucket checksums-example-vs1 \
--key myfilecrc.txt \
--body myfile.txt \
--checksum-algorithm="CRC32" \
--checksum-crc32="e7c80b87"
```