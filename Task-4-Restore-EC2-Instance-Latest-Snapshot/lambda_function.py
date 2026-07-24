import boto3
from datetime import datetime

ec2 = boto3.client("ec2")

# Change these values
VOLUME_ID = "vol-xxxxxxxx"
SUBNET_ID = "subnet-xxxxxxxx"
SECURITY_GROUP = "sg-xxxxxxxx"

def lambda_handler(event, context):

    snapshots = ec2.describe_snapshots(
        Filters=[
            {
                "Name": "volume-id",
                "Values": [VOLUME_ID]
            }
        ],
        OwnerIds=["self"]
    )["Snapshots"]

    if not snapshots:
        raise Exception("No snapshots found.")

    latest_snapshot = sorted(
        snapshots,
        key=lambda x: x["StartTime"],
        reverse=True
    )[0]

    snapshot_id = latest_snapshot["SnapshotId"]

    ami_name = f"RestoreAMI-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"

    image = ec2.register_image(
        Name=ami_name,
        RootDeviceName="/dev/xvda",
        VirtualizationType="hvm",
        Architecture="x86_64",
        BlockDeviceMappings=[
            {
                "DeviceName": "/dev/xvda",
                "Ebs": {
                    "SnapshotId": snapshot_id,
                    "DeleteOnTermination": True,
                    "VolumeType": "gp3"
                }
            }
        ]
    )

    image_id = image["ImageId"]

    print(f"AMI Created: {image_id}")

    waiter = ec2.get_waiter("image_available")
    waiter.wait(ImageIds=[image_id])

    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType="t3.micro",
        MinCount=1,
        MaxCount=1,
        SubnetId=SUBNET_ID,
        SecurityGroupIds=[SECURITY_GROUP],
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "Restored-EC2"
                    },
                    {
                        "Key": "RestoredFrom",
                        "Value": snapshot_id
                    }
                ]
            }
        ]
    )

    instance_id = response["Instances"][0]["InstanceId"]

    print(f"New Instance: {instance_id}")

    return {
        "statusCode": 200,
        "Snapshot": snapshot_id,
        "AMI": image_id,
        "Instance": instance_id
    }
