import boto3,logging,json,os
from botocore.config import Config

POWERFUL_ACTIONS = ["config:DeleteConfigRule","lambda:AddPermission","lambda:DeleteFunction","lambda:InvokeFunction",
                    "kms:CreateKey","kms:Decrypt","kms:DisableKey","athena:DeleteNamedQuery","dynamodb:CreateBackup",
                    "dynamodb:DeleteBackup","dynamodb:DeleteItem","dynamodb:DeleteTable","dax:DeleteCluster","dax:DeleteItem",
                    "dax:DeleteParameterGroup","dax:DeleteSubnetGroup","dax:RebootNode","ec2:CreateCustomerGateway",
                    "ec2:CreateDefaultSubnet","ec2:CreateDefaultVpc","ec2:CreateDhcpOptions","ec2:CreateEgressOnlyInternetGateway",
                    "ec2:CreateNetworkAcl","ec2:CreateNetworkAclEntry","ec2:CreateRoute","ec2:CreateRouteTable","ec2:CreateSubnet",
                    "ec2:CreateVpc","ec2:CreateVpcEndpoint","ec2:DeleteCustomerGateway","ec2:DeleteDhcpOptions","ec2:DeleteEgressOnlyInternetGateway",
                    "ec2:DeleteFlowLogs","ec2:DeleteNetworkAcl","ec2:DeleteNetworkAclEntry","ec2:DeleteRoute","ec2:DeleteRouteTable",
                    "ec2:DeleteSecurityGroup","ec2:DeleteSubnet","ec2:DeleteVpc","ec2:DeleteVpcEndpoints","ec2:DeleteVpcPeeringConnection",
                    "ec2:DeleteVpnConnection","ec2:DeleteVpnConnectionRoute","ec2:DeleteVpnGateway","cloudformation:DeleteStack","iam:DeleteSAMLProvider",
                    "iam:DeleteSSHPublicKey"]

session = boto3.Session(profile_name='default', region_name='us-east-2')
iam_client = session.client('iam')

# All IAM Users
try:
    allIamUsers = iam_client.list_users().get('Users',[])
    userList = []
    for iamUser in allIamUsers:
        userdata = {
            'UserName': iamUser['UserName'],
            'UserArn': iamUser['Arn']
        }
        userList.append(userdata)
    print(userList)

except Exception as e:
    raise Exception("[ErrorMessage]: " + str(e))

# All IAM Groups
try:
    allIamGroups = iam_client.list_groups().get('Groups',[])
    groupList = []    
    for iamGroup in allIamGroups:
        groupData = {
            'GroupName': iamGroup['GroupName'],
            'GroupArn': iamGroup['Arn']
        }
        groupList.append(groupData)
    print(groupList)
        
except Exception as e:
    raise Exception("[ErrorMessage]: " + str(e))

# All IAM Roles
try:
    allIamRoles = iam_client.list_roles().get('Roles',[])
    roleList = []
    for iamRole in allIamRoles:
        roleData={
            'RoleName': iamRole['RoleName'],
            'RoleArn': iamRole['Arn']
        }
        roleList.append(roleData)
        
except Exception as e:
    raise Exception("[ErrorMessage]: " + str(e))

# All IAM Policies    
try:
    allIamPolicies = iam_client.list_policies().get('Policies',[])
    for iamPolicy in allIamPolicies:
        print(iamPolicy['PolicyName'])
        
except Exception as e:
    raise Exception("[ErrorMessage]: " + str(e))

# all_simlumation_results = iam_client.simulate_principal_policy(
#     PolicySourceArn = 'arn:aws:iam:::user/s3apicreate',
#     ActionNames = POWERFUL_ACTIONS    
# ).get('EvaluationResults',[])

# for simulation_result in all_simlumation_results:
#     if simulation_result['EvalDecision'] == 'allowed':
#         print(simulation_result)    