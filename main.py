from modules.aws_inventory import get_aws_inventory
from modules.cost_optimizer import find_unused_resources

import subprocess

print("""
==================================
 AI CLOUD OPS ASSISTANT
==================================

1. AWS Inventory
2. Cost Optimizer
3. AI Cloud Auditor
""")

choice = input("Select option: ")

if choice == "1":
    print(get_aws_inventory())

elif choice == "2":
    print(find_unused_resources())

elif choice == "3":
    subprocess.run(["python", "modules/ai_auditor.py"])

else:
    print("Invalid choice")
