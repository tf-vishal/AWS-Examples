package main

import (
	"context"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

// Function to create a bucket
func createBucket(bucketName string, region string) error {
	// Load the AWS configuration
	cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithRegion(region))
	if err != nil {
		return fmt.Errorf("failed to load AWS configuration: %w", err)
	}

	// Create an S3 client
	s3Client := s3.NewFromConfig(cfg)

	// Create the bucket
	_, err = s3Client.CreateBucket(context.TODO(), &s3.CreateBucketInput{
		Bucket: aws.String(bucketName),
	})
	if err != nil {
		return fmt.Errorf("failed to create bucket: %w", err)
	}

	fmt.Printf("Bucket '%s' created successfully in region '%s'.\n", bucketName, region)
	return nil
}

func main() {
	// Specify the bucket name and region
	bucketName := "example-go-bucket"
	region := "us-east-1"
	fmt.Printf("Hello")

	// Call the createBucket function
	err := createBucket(bucketName, region)
	if err != nil {
		log.Fatalf("Error creating bucket: %v", err)
	}
}
