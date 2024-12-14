import boto3
from botocore.exceptions import ClientError

def createBucket(bucketname,region):
    s3=boto3.resource("s3")

    try:
         print("\nCreating new bucket:", bucketname)
         bucket = s3.create_bucket(
              Bucket = bucketname,
              CreateBucketConfiguration={
                   "LocationConstraint": s3.meta.client.meta.region_name
                   },
                )
    except ClientError as e:
        print(
            f"Couldn't create a bucket for the demo. Here's why: "
            f"{e.response['Error']['Message']}"
        )
        raise

if __name__ == "__main__":
    bucketname = input("Type the bucketname-")
    region = input("Type the region")
    createBucket(bucketname,region)