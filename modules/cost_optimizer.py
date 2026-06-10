import boto3

def find_unused_resources():
    ec2 = boto3.client("ec2")

    report = []

    # Stopped instances
    instances = ec2.describe_instances()

    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:

            if instance["State"]["Name"] == "stopped":
                report.append(
                    f"Stopped EC2 instance: {instance['InstanceId']}"
                )

    # Unattached volumes
    volumes = ec2.describe_volumes()

    for volume in volumes["Volumes"]:
        if len(volume["Attachments"]) == 0:
            report.append(
                f"Unattached EBS volume: {volume['VolumeId']}"
            )

    return report


if __name__ == "__main__":
    findings = find_unused_resources()

    print("\nAWS Cost Optimization Report\n")

    if findings:
        for item in findings:
            print("-", item)
    else:
        print("No obvious unused resources found.")
