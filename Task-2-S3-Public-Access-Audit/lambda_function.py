import boto3

s3 = boto3.client("s3")
sns = boto3.client("sns")

SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:279473426275:S3PublicBucketAlert"


def lambda_handler(event, context):

    buckets = s3.list_buckets()["Buckets"]

    public_buckets = []

    for bucket in buckets:

        bucket_name = bucket["Name"]

        issues = []

        # Check Block Public Access
        try:
            block = s3.get_public_access_block(Bucket=bucket_name)

            config = block["PublicAccessBlockConfiguration"]

            if not all(config.values()):
                issues.append("Block Public Access Disabled")

        except Exception:
            issues.append("Block Public Access Not Configured")

        # Check Bucket Policy
        try:
            status = s3.get_bucket_policy_status(Bucket=bucket_name)

            if status["PolicyStatus"]["IsPublic"]:
                issues.append("Bucket Policy is Public")

        except Exception:
            pass

        # Check ACL
        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)

            for grant in acl["Grants"]:

                grantee = grant.get("Grantee", {})

                uri = grantee.get("URI", "")

                if "AllUsers" in uri or "AuthenticatedUsers" in uri:
                    issues.append("Public ACL")
                    break

        except Exception:
            pass

        if issues:
            public_buckets.append(f"{bucket_name}: {', '.join(issues)}")

    if public_buckets:

        message = "Public S3 Buckets Found:\n\n"

        message += "\n".join(public_buckets)

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="S3 Public Bucket Alert",
            Message=message
        )

        print(message)

    else:
        print("No public buckets found.")

    return {
        "statusCode": 200,
        "body": "Audit Complete"
    }
