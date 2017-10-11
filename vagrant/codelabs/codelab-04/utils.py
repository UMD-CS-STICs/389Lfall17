import botocore
import boto3
import json
import time

from os.path import basename

from config import *

s3 = boto3.resource('s3')
sqs = boto3.resource('sqs')
ec2 = boto3.resource('ec2')

s3_client = boto3.client('s3')
ec2_client = boto3.client('ec2')
iam_client = boto3.client('iam')

# SQS


def initialize_queue(queue_name, dlq_name):
    """Initialize an SQS queue and Dead-Letter queue.

    Messages will be dropped into the DLQ after 3 receives.

    Args:
        queue_name (string): Name of SQS queue to create.
        dlq_name (string): Name of SQS dead-letter queue to create.

    Returns:
        SQS.Queue object of the SQS queue that was created.
    """
    # TODO(you)
    pass


# S3


def initialize_bucket(bucket_name, acl='private'):
    """Initialize an S3 bucket with the specified ACL.

    Args:
        bucket_name (string): Name of bucket to create.
        acl (string): Name of ACL to use.

    Returns:
        S3.Bucket object that was created.
    """
    bucket = s3_client.create_bucket(Bucket=bucket_name, ACL=acl)
    return bucket


def upload_s3_file(bucket, file, content_type, acl='private'):
    """Upload a file to an S3 bucket.

    Args:
        bucket (string): Name of the bucket to upload the file to.
        file (string): Relative path to the file. Basename used as key.
        content_type (string): Content-Type to associate with the file.
        acl (string): ACL to give to S3 file.
    """
    key = basename(file)
    with open(file, 'rb') as f:
        s3.Bucket(bucket).put_object(Body=f.read(), Key=key,
                                     ACL=acl, ContentType=content_type)


def download_s3_file(bucket, key, dest):
    """Downloads a file from an S3 bucket into a destination directory.

    Args:
        bucket (string): Name of the bucket to download from.
        key (string): Key of the object to download.
        dest (string): Relative directory path to download the file into.

    Returns:
        Relative path to the downloaded file.
    """
    output_path = join(dest, basename(key))
    print('Downloading image from {} to {}'.format(
        (join(bucket, key)), output_path))
    s3.Bucket(bucket).download_file(key, output_path)

    return output_path

# IAM


def initialize_instance_profile(role_name, instance_profile_name):
    """Initialize an EC2 instance profile with the specified role name.

    A role will be attached to the instance profile that has two attached policies:
    - AmazonS3FullAccess
    - AmazonSQSFullAccess

    Args:
        role_name (string): Name of the role to create.
        instance_profile_name (string): Name of the instance profile to create.
    """
    iam_client = boto3.client('iam')

    assume_role_doc = json.dumps({
        'Statement': [{
            'Effect': 'Allow',
            'Principal': {
                'Service': 'ec2.amazonaws.com'
            },
            'Action': 'sts:AssumeRole'
        }]
    })

    iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=assume_role_doc)

    iam_client.attach_role_policy(
        PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess',
        RoleName=role_name
    )

    iam_client.attach_role_policy(
        PolicyArn='arn:aws:iam::aws:policy/AmazonSQSFullAccess',
        RoleName=role_name
    )

    iam_client.create_instance_profile(
        InstanceProfileName=instance_profile_name
    )

    iam_client.add_role_to_instance_profile(
        InstanceProfileName=instance_profile_name,
        RoleName=role_name)

# Security Group


def initialize_ssh_security_group(security_group):
    """Initialize a security group that opens inbound SSH.

    Args:
        security_group (string): Name of the SSH security group to create.
    """
    # Create the security group
    response = ec2_client.create_security_group(
        GroupName=security_group,
        Description='SSH open to all IPs')

    # Authorize inbound SSH traffic
    security_group_id = response['GroupId']
    data = ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[{
            'IpProtocol': 'tcp',
            'FromPort': SSH_PORT,
            'ToPort': SSH_PORT,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }])

# EC2


def initilize_server(security_group, keypair=None):
    """Initializes an Ubuntu 16.04 t2.micro for the thumbnailer.

    The instance is configured with a "codelab-04" tag to make it easy to find and clean up. It also has the previously generated instance profile attached, along with the SSH security group. It will execute the setup.sh script on launch as user data.

    Args:
        security_group (string): Name of the SSH security group to create.
        keypair (string): Name of the keypair to associate with the instance. If None, no keypair is used.

    Returns:
        EC2.Instance object of the created instance.
    """
    with open('scripts/ec2_setup.sh', 'r') as f:
        init_commands = f.read().format(username=USERNAME)

        instances = ec2.create_instances(
            ImageId='ami-cd0f5cb6',
            InstanceType='t2.micro',
            KeyName=keypair,
            MinCount=1,
            MaxCount=1,
            SecurityGroups=[security_group],
            UserData=init_commands,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{
                    'Key': EC2_TAG_KEY,
                    'Value': EC2_TAG_VALUE,
                }]
            }],
            IamInstanceProfile={
                'Name': S3_INSTANCE_PROFILE_NAME
            })

        assert(len(instances) == 1)
        instance = instances[0]

        _wait_on_server(instance)

        return instance


def _wait_on_server(instance):
    """Wrapper on AWS wrapper to wait on a server to start running.

    Args:
        instance (EC2.instance): Instance to wait on.
    """
    print('Waiting on instance {}: {}'.format(
        instance.id, instance.state['Name']))

    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance.id])

    instance.reload()
    print('Instance {}: running ({})'.format(
        instance.id, instance.public_ip_address))
