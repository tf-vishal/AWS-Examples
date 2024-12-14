import boto3
from botocore.exceptions import ClientError

def deleteBucket(bucketname):
    s3=boto3.resource("s3")
    bucket= s3.Bucket(bucketname)

    try:
        #attempt to delete the bucket
        print(f"Attempting to delete bucket :{bucketname}")
        bucket.delete()
        print(f" {bucketname} has successfully deleted")
    except ClientError as e:
        print(f"Couldn't delete the bucket. Here's why: {e.response['Error']['Message']}")
        raise

if __name__ == "__main__":
    bucketname = input("Type the bucketname-")
    deleteBucket(bucketname)