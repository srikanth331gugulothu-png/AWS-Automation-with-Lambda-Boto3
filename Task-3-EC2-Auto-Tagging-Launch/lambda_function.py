import boto3
from datetime import datetime

ec2 = boto3.client("ec2")


def lambda_handler(event, context):

    print("Received Event:")
    print(event)

    instance_id = event["detail"]["instance-id"]

    today = datetime.utcnow().strftime("%Y-%m-%d")

    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {
                "Key": "LaunchDate",
                "Value": today
            },
            {
                "Key": "Environment",
                "Value": "Dev"
            }
        ]
    )

    print(f"Tags added successfully to {instance_id}")

    return {
        "statusCode": 200,
        "body": f"Tagged {instance_id}"
    }
