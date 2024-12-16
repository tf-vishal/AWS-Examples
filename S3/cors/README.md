# AWS S3 CORS Examples

## Create Website 1

### Create a Bucket
To create a new S3 bucket, use the following command:

```sh
aws s3 mb s3://cors-fun-vs1
```

### Change Block Public Access
To configure the bucket's public access settings:

```sh
aws s3api put-public-access-block \
--bucket cors-fun-vs1 \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

[Documentation for `put-public-access-block`](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-public-access-block.html)

### Create a Bucket Policy
To apply a bucket policy, use the following command:

```sh
aws s3api put-bucket-policy --bucket cors-fun-vs1 --policy file:///home/muzan/AWS-Examples/S3/cors/policy/bucketpolicy.json
```

[Documentation for `put-bucket-policy`](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-policy.html)

Refer to the [JSON policy documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html) for more details.

### Turn on Static Website Hosting
Enable static website hosting with the following command:

```sh
aws s3api put-bucket-website --bucket cors-fun-vs1 --website-configuration file:///home/muzan/AWS-Examples/S3/cors/policy/website.json
```

[Documentation for `put-bucket-website`](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-website.html)

### Upload `index.html` File
Upload an `index.html` file that includes a resource requiring cross-origin access:

```sh
aws s3 cp ./pages/index.html s3://cors-fun-vs1
```

### View the Website
To verify the website, navigate to one of the following URLs:

- `http://cors-fun-vs1.s3-website-ap-south-1.amazonaws.com`
- `http://cors-fun-vs1.s3-website.ap-south-1.amazonaws.com`

---

## Create Website 2

### Create a Bucket
To create another S3 bucket, use the following command:

```sh
aws s3 mb s3://cors-fun-vs2
```

### Change Block Public Access
To configure the bucket's public access settings:

```sh
aws s3api put-public-access-block \
--bucket cors-fun-vs2 \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

[Documentation for `put-public-access-block`](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-public-access-block.html)

### Create a Bucket Policy
To apply a bucket policy, use the following command:

```sh
aws s3api put-bucket-policy --bucket cors-fun-vs2 --policy file:///home/muzan/AWS-Examples/S3/cors/policy/bucketpolicy2.json
```

[Documentation for `put-bucket-policy`](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-policy.html)

Refer to the [JSON policy documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html) for more details.

### Turn on Static Website Hosting
Enable static website hosting with the following command:

```sh
aws s3api put-bucket-website --bucket cors-fun-vs2 --website-configuration file:///home/muzan/AWS-Examples/S3/cors/policy/website.json
```

[Documentation for `put-bucket-website`](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-website.html)

### Upload `hello.js` File
Upload a `hello.js` file to the bucket:

```sh
aws s3 cp ./pages/hello.js s3://cors-fun-vs2
```