import boto3
from datetime import datetime

ec2 = boto3.client("ec2")

def lambda_handler(event, context):

    print("Received Event:", event)

    if "detail" not in event:
        return {
            "statusCode": 400,
            "body": "This Lambda must be invoked by EventBridge."
        }

    instance_id = event["detail"]["instance-id"]

    today = datetime.utcnow().strftime("%Y-%m-%d")

    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {"Key": "LaunchDate", "Value": today},
            {"Key": "Environment", "Value": "Dev"}
        ]
    )

    print(f"Tagged {instance_id}")

    return {
        "statusCode": 200,
        "body": f"Tagged {instance_id}"
    }
      
