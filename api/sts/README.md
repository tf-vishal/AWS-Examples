# AWS S3 Bucket Encryption Management

This document provides AWS CLI commands to manage server-side encryption for S3 buckets and objects, including KMS and customer-provided encryption keys.
> Errors are there
---

## Create a Bucket
To create a new S3 bucket:

```sh
aws s3 mb s3://encrypt-fun-vs1
```

---

## Create a File and Upload to S3
To create a file and upload it to the S3 bucket:

```sh
echo "hello world" > hello.txt
aws s3 cp hello.txt s3://encrypt-fun-vs1
```

---

## Put Object with KMS Encryption
To upload an object with AWS KMS encryption enabled:

```sh
aws s3api put-object \
--bucket encrypt-fun-vs1 \
--key hello.txt --body hello.txt \
--server-side-encryption aws:kms \
--ssekms-key-id 27b3f7f3-a192-46c2-8df3-a1593530a234
```

![Encrypt SS](./images/image.png)

---

## List Existing KMS Keys
To list all available KMS keys:

```sh
aws kms list-keys
```

![After changing the encryption method](./images/image-1.png)

---

## Put Object with SSE-C (Failed Attempt)
This section demonstrates a failed attempt to use customer-provided encryption keys (SSE-C) due to MD5 hash issues.

### Generate OpenSSL Key
First, create a base64-encoded encryption key:

```sh
export BASE64_ENCODED_KEY=$(openssl rand base64 32) 
echo $BASE64_ENCODED_KEY
```

### Generate MD5 Hash
Create an MD5 hash of the base64 key:

```sh
export MD5_VALUE=$(echo -n $BASE_ENCODED_KEY | md5sum | awk '{print $1}' | base64 -w0)
echo $MD5_VALUE
```

### Put Object Command (Failed)

```sh
aws s3api put-object \
--bucket encrypt-fun-vs1 \
--key hello.txt --body hello.txt \
--sse-customer-algoritm AES256 \
--sse-customer-key $BASE64_ENCODED_KEY \
--sse-customer-md5 $MD5_VALUE
```

**Error**: `The calculated MD5 hash of the key did not match the hash that was provided.`

---

## Put Object with SSE-C via AWS S3
To successfully upload an object with SSE-C, follow these steps.

### Generate an Encryption Key
Create a 32-byte key and save it to a file:

```sh
openssl rand -out ssec.key 32
```

### Upload an Object with SSE-C
Upload the object using the generated key:

```sh
aws s3 cp hello.txt s3://encrypt-fun-vs1/hello.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```

### Download the Encrypted Object
To download the object, the key is required:

```sh
aws s3 cp s3://encrypt-fun-vs1/hello.txt hello.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```

---

## Create a User with No Permissions
To create a new user with no permissions and generate access keys:

```sh
aws iam create-user --user-name sts-machine-user
aws iam create-access-key --user-name sts-machine-user --output table
```

Copy the access key and secret into your AWS credentials file:

```sh
aws configure
```

Then edit the credentials file to change the profile:

```sh
open ~/.aws/credentials 
```

Test the credentials:

```sh
aws sts get-caller-identity
aws sts get-caller-identity --profile sts
```

Make sure the user cannot access S3:

```sh
aws s3 ls --profile sts
```

> An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied

---

## Create a Role
To create a role that grants access to a new resource:

```sh
chmod u+x bin/deploy
./bin/deploy
```

---

## Use New User Credentials and Assume Role
Attach a policy to allow the user to assume a role:

```sh
aws iam put-user-policy \
--user-name sts-machine-user  \
--policy-name StsAssumePolicy \
--policy-document file://policy.json
```

Assume the role:

```sh
aws sts assume-role \
--role-arn arn:aws:iam::982383527471:role/my-sts-fun-stack-StsRole-UBQlCIzagA7n \
--role-session-name s3-sts-fun \
--profile sts
```

Test the assumed role credentials:

```sh
aws sts get-caller-identity --profile assumed
aws s3 ls --profile assumed
```

---

## Cleanup
To remove the user, policies, and keys:

```sh
aws iam delete-user-policy --user-name sts-machine-user --policy-name StsAssumePolicy
aws iam delete-access-key --access-key-id AKIA6JOU7AYXR3PVODP3 --user-name sts-machine-user
aws iam delete-user --user-name sts-machine-user
```

### Cleanup Everything
To delete all files and the bucket:

```sh
aws s3 rm s3://encrypt-fun-vs1/hello.txt
aws s3 rb s3://encrypt-fun-vs1
```
