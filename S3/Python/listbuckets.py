import boto3

def hello_s3():
    s3 = boto3.resource("s3")
    print("Hello AWS,List all ur buckets")
    for bucket in s3.buckets.all():
        print(f"\t{bucket.name}")

if __name__ == "__main__":
    hello_s3()