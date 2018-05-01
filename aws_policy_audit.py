import boto3
import os

# session = boto3.session.Session(profile_name='default')
session = boto3.Session(profile_name='default')
iam = session.client('iam')
account_id = boto3.client('sts').get_caller_identity().get('Account')
result = iam.simulate_principal_policy(
    PolicySourceArn="arn:aws:iam::"+account_id+":role/aws_network_admins",
    ResourceArns=["*"],
    ActionNames=["ec2:*"]
)
print(result.get('EvaluationResults',[]))
