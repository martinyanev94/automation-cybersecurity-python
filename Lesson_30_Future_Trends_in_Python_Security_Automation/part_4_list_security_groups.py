import boto3

def list_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()
    
    for group in response['SecurityGroups']:
        print(f"Group Name: {group['GroupName']}, ID: {group['GroupId']}")
        for permission in group['IpPermissions']:
            print(f"  IP Protocol: {permission['IpProtocol']}, From Port: {permission.get('FromPort', 'N/A')}, To Port: {permission.get('ToPort', 'N/A')}")

list_security_groups()
