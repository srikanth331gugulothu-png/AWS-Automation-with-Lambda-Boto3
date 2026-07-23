
Task-6-S3-Public-Access-Audit/
│
├── README.md
│   └── Project documentation, architecture, setup instructions,
│       testing steps, and expected outputs.
│
├── lambda_function.py
│   └── AWS Lambda function that:
│       • Lists all S3 buckets
│       • Checks Block Public Access configuration
│       • Checks Bucket Policy Status (IsPublic)
│       • Checks Bucket ACLs
│       • Publishes an SNS alert if any bucket is insecure
│
├── bucketpolicy.json
│   └── Sample public-read bucket policy used only for testing
│       public bucket detection.
│
└── screenshots/
    ├── 01-s3-buckets.png
    ├── 02-sns-topic.png
    ├── 03-email-subscription.png
    ├── 04-iam-role.png
    ├── 05-lambda-function.png
    ├── 06-lambda-code.png
    ├── 07-test-event.png
    ├── 08-cloudwatch-logs.png
    ├── 09-eventbridge-rule.png
    ├── 10-public-bucket-policy.png
    └── 11-sns-email-alert.png
```
