
AWS Automation
# AWS Automation with Lambda & Boto3

This repository contains hands-on AWS automation projects built using **AWS Lambda**, **Python (Boto3)**, and other AWS services. Each project demonstrates how to automate common cloud administration tasks such as S3 management, EC2 automation, and disaster recovery.

## Technologies Used

- AWS Lambda
- Python 3.x
- Boto3
- Amazon EC2
- Amazon EBS
- Amazon S3
- Amazon SNS
- Amazon EventBridge
- AWS IAM
- Amazon CloudWatch

---

## Repository Structure

```
AWS-Automation-with-Lambda-Boto3/
│
├── Task-1-S3-Bucket-Cleanup/
│   ├── lambda_function.py
│   ├── README.md
│   ├── architecture.png
│   └── screenshots/
│
├── Task-2-S3-Public-Access-Audit/
│   ├── lambda_function.py
│   ├── bucketpolicy.json
│   ├── README.md
│   ├── architecture.png
│   └── screenshots/
│
├── Task-3-EC2-Auto-Tagging-Launch/
│   ├── lambda_function.py
│   ├── README.md
│   ├── architecture.png
│   └── screenshots/
│
├── Task-4-Restore-EC2-Instance-Latest-Snapshot/
│   ├── lambda_function.py
│   ├── README.md
│   ├── architecture.png
│   └── screenshots/
│
└── README.md
```

---

# Projects

## Task 1 – S3 Bucket Cleanup

### Objective

Automatically delete S3 objects older than a specified retention period to reduce storage costs and maintain bucket hygiene.

### AWS Services

- Amazon S3
- AWS Lambda
- Amazon EventBridge
- IAM
- CloudWatch Logs

### Features

- Scans S3 buckets
- Deletes objects older than the configured retention period
- Supports nested folders
- Logs deleted objects
- Runs automatically on schedule

---

## Task 2 – Audit S3 Buckets for Public Access

### Objective

Automatically audit S3 buckets for public access and notify administrators whenever a public bucket is detected.

### AWS Services

- Amazon S3
- AWS Lambda
- Amazon SNS
- Amazon EventBridge
- IAM

### Features

- Scans all S3 buckets
- Detects public bucket policies and ACLs
- Sends SNS email notifications
- Logs audit results in CloudWatch
- Scheduled daily execution

---

## Task 3 – Auto Tag EC2 Instances on Launch

### Objective

Automatically apply standard tags to newly launched EC2 instances using EventBridge and AWS Lambda.

### AWS Services

- Amazon EC2
- AWS Lambda
- Amazon EventBridge
- IAM
- CloudWatch Logs

### Features

- Detects new EC2 instance launches
- Automatically adds predefined tags
- Improves resource organization
- Supports cost allocation and governance
- Fully serverless automation

---

## Task 4 – Restore EC2 Instance from Latest Snapshot

### Objective

Automatically restore an EC2 instance using the most recent EBS snapshot by creating an AMI and launching a replacement instance.

### AWS Services

- Amazon EC2
- Amazon EBS
- AWS Lambda
- IAM
- CloudWatch Logs

### Features

- Finds the latest snapshot
- Registers an AMI from the snapshot
- Launches a new EC2 instance
- Automatically tags the restored instance
- Prints the restored instance ID
- Supports disaster recovery automation

---

# Learning Outcomes

These projects demonstrate practical experience with:

- AWS Lambda
- Python Boto3 SDK
- Amazon EC2 Automation
- Amazon EBS Snapshot Management
- Amazon S3 Management
- Event-Driven Architecture
- Amazon SNS Notifications
- IAM Roles and Policies
- EventBridge Scheduling
- CloudWatch Monitoring
- Infrastructure Automation
- Disaster Recovery

---

# Prerequisites

- AWS Account
- IAM User with Administrator Access (for lab/testing)
- Python 3.x
- Boto3
- knowledge of AWS services

---

# Deployment Steps

1. Create the required IAM role.
2. Create the Lambda function.
3. Attach the IAM role.
4. Configure EventBridge trigger or Test Event.
5. Deploy the Lambda function.
6. Execute the function.
7. Verify CloudWatch logs.
8. Validate the AWS resources.

---

# Cleanup

- Deleted Lambda functions
- Deleted EventBridge rules
- Removed SNS topics
- Deleted test S3 buckets
- Deleted temporary snapshots
- Deregisterd temporary AMIs
- Terminated EC2 test instances
- Removed unused IAM roles and policies

---

# Author

**Srikanth Gugulothu**

https://github.com/srikanth331gugulothu-png/AWS-Automation-with-Lambda-Boto3

---
