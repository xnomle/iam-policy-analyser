import boto3
import os
import json
from parliament import analyze_policy_string
from dotenv import load_dotenv 

load_dotenv()

access_key = os.getenv("AWS_ACCESS_KEY_ID")
secrect_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_DEFAULT_REGION")

IAM_CLIENT = boto3.client('iam')

def return_arn():
    response = IAM_CLIENT.list_policies(
    Scope='Local',
    MaxItems = 1
    )

    for policy in response["Policies"]:
        return(policy["Arn"], policy["DefaultVersionId"])


def get_iam_policy(Arn, DefaultVersionId):
    response = IAM_CLIENT.get_policy_version(
    PolicyArn=Arn,
    VersionId=DefaultVersionId
)
    
    return(json.dumps(response["PolicyVersion"]["Document"], default=str, indent=4))



def main():
    Arn, DefaultVersionId = return_arn()
    iam_policy = get_iam_policy(Arn, DefaultVersionId)
    policy = analyze_policy_string(iam_policy)
    for finding in policy.findings:
        print(json.dumps(finding, indent=4, default=str))

                
main()
            
#print(json.dumps(response,indent=4, default=str))
#print(policy["PolicyName"])
#print(json.dumps(policy.PolicyName ,indent=4, default=str))
#print(json.dumps(response, indent= 4, default=str))
