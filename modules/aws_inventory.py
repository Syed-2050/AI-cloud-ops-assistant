import boto3
import json

def get_aws_inventory():
    ec2 = boto3.client("ec2")
    s3 = boto3.client("s3")
    iam = boto3.client("iam")

    inventory = {
        "ec2_instances": [],
        "s3_buckets": [],
        "iam_users": []
    }

    # EC2
    instances = ec2.describe_instances()

    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            inventory["ec2_instances"].append({
                "instance_id": instance["InstanceId"],
                "state": instance["State"]["Name"],
                "instance_type": instance["InstanceType"]
            })

    # S3
    buckets = s3.list_buckets()

    for bucket in buckets["Buckets"]:
        inventory["s3_buckets"].append(bucket["Name"])

    # IAM
    users = iam.list_users()

    for user in users["Users"]:
        inventory["iam_users"].append(user["UserName"])

    return inventory


if __name__ == "__main__":
    data = get_aws_inventory()

    print(json.dumps(data, indent=2))
