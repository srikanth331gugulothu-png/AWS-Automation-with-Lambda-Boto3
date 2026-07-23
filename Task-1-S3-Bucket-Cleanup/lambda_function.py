import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client("s3")

BUCKET_NAME = "srikanth-s3-cleanup-demo"

# Production
AGE_LIMIT = timedelta(days=30)

# For Testing
# AGE_LIMIT = timedelta(minutes=5)

def lambda_handler(event, context):

    now = datetime.now(timezone.utc)

    paginator = s3.get_paginator("list_objects_v2")

    deleted_objects = []

    for page in paginator.paginate(Bucket=BUCKET_NAME):

        if "Contents" not in page:
            continue

        for obj in page["Contents"]:

            key = obj["Key"]
            last_modified = obj["LastModified"]

            if now - last_modified > AGE_LIMIT:

                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=key
                )

                deleted_objects.append(key)

                print(f"Deleted: {key}")

    return {
        "statusCode": 200,
        "deleted_objects": deleted_objects,
        "total_deleted": len(deleted_objects)
    }
