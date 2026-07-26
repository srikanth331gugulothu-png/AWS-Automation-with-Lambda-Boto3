import boto3
from datetime import date

ce = boto3.client("ce")
sns = boto3.client("sns")

THRESHOLD = 50  # Change to 50 for production

TOPIC_ARN = "arn:aws:sns:us-east-1:279473426275:DailyAWSCostAlert"


def lambda_handler(event, context):

    today = date.today()

    start = today.replace(day=1).strftime("%Y-%m-%d")
    end = today.strftime("%Y-%m-%d")

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start,
            "End": end
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    amount = float(
        response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]
    )

    print(f"Current Month Cost: ${amount:.2f}")

    if amount > THRESHOLD:

        message = f"""
AWS Cost Alert

Current Month Spend : ${amount:.2f}

Threshold : ${THRESHOLD:.2f}

Please review your AWS resources.
"""

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="AWS Daily Cost Alert",
            Message=message
        )

        print("Alert Sent")

    else:
        print("Cost below threshold")

    return {
        "statusCode": 200,
        "body": amount
    }
