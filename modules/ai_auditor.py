import boto3
import requests
import json

def get_inventory():
    s3 = boto3.client("s3")
    iam = boto3.client("iam")

    data = {
        "s3_buckets": [],
        "iam_users": []
    }

    for bucket in s3.list_buckets()["Buckets"]:
        data["s3_buckets"].append(bucket["Name"])

    for user in iam.list_users()["Users"]:
        data["iam_users"].append(user["UserName"])

    return data


inventory = get_inventory()

prompt = f"""
You are an AWS Cloud Architect.

Analyze this AWS account inventory and provide:

1. Security observations
2. Cost optimization suggestions
3. Best practice recommendations
4. Risk assessment

AWS Data:
{json.dumps(inventory, indent=2)}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()

print("\n===== AI CLOUD AUDIT REPORT =====\n")

if "response" in result:
    print(result["response"])
else:
    print(result)
