# AWS CodeBase
   A collection of examples and scripts for working with AWS services such as S3, EC2, Lambda, and more.

   ---

## Prerequities
   Before starting, make sure you have the following:
   - An **AWS account**: If you don’t have one, sign up at [AWS](https://aws.amazon.com/).
   - **AWS CLI**: Install the AWS Command Line Interface on your local machine. Follow the installation guide: [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
   - **IAM User Permissions**: Ensure your AWS user has the appropriate permissions to access services (EC2, S3, etc.). You can create and configure IAM users from the [IAM console](https://console.aws.amazon.com/iam/home).

   ## GitHub Setup
   - **Git**: Install Git from [here](https://git-scm.com/).
   - **GitHub Account**: You’ll need a GitHub account. If you don’t have one, sign up at [GitHub](https://github.com/).
   - **AWS CLI**: If your project needs integration with AWS, ensure the AWS CLI is configured (see [AWS Setup Documentation](#aws-setup-documentation)).
---
## Setup
---
   ### **1. Configure AWS CLI**
   Once you’ve installed the AWS CLI, configure it with your AWS credentials:
```bash
aws configure
```
---
   ### **2. GitHub Setup** 
   How to create repository on github and clone it and connect it
   #### 1. Create a New GitHub Repository

1. Go to [GitHub](https://github.com/).
2. Click on the **+** in the top-right corner and select **New repository**.
3. Choose a repository name (e.g., `AWS-Examples`).
4. Optionally, add a description for the repository.
5. Choose **Public** or **Private** for your repository.
6. Select **Initialize this repository with a README** (optional).
7. Click **Create repository**.



#### **2. Clone the Repository to Your Local Machine**
   To clone the repository, use the following command:
```bash
git clone https://github.com/username/AWS-Examples.git
