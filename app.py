import boto3
import os
import json
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
        #print(policy["Arn"])
        return(policy["Arn"], policy["DefaultVersionId"])


def get_iam_policy(Arn, DefaultVersionId):
    response = IAM_CLIENT.get_policy_version(
    PolicyArn=Arn,
    VersionId=DefaultVersionId
)
    print(json.dumps(response, default=str, indent=4))



def main():
    Arn, DefaultVersionId = return_arn()
    get_iam_policy(Arn, DefaultVersionId)
                
main()
            
#print(json.dumps(response,indent=4, default=str))
#print(policy["PolicyName"])
#print(json.dumps(policy.PolicyName ,indent=4, default=str))
#print(json.dumps(response, indent= 4, default=str))
