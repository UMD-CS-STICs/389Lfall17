"""Setup script for the image thumbnailing service."""

import argparse
import time

from os.path import join

from config import *
from utils import initialize_queue, initialize_bucket, upload_s3_file, initialize_instance_profile, initialize_security_group, initilize_server


def setup(args):
    """Initializes the environment for the image thumbnailing service."""

    # Create an SQS queue with a Dead-Letter queue for thumbnailing requests.
    if args.queue or args.all:
        queue = initialize_queue(SQS_QUEUE_NAME, DLQ_NAME)
        print('SQS Queue: {}'.format(queue.url))

    # Create an S3 bucket for thumbnails, and
    # another to transfer thumbnailing code to an EC2 instance.
    if args.buckets or args.all:
        thumbnails = initialize_bucket(S3_OUTPUT_BUCKET, acl='public-read')
        print('S3 thumbnail bucket: {}'.format(thumbnails['Location']))
        code = initialize_bucket(S3_CODE_BUCKET)
        print('S3 code bucket: {}'.format(code['Location']))

    # Upload image thumbnailing code to S3.
    if args.upload_code or args.all:
        for file in CODE_FILES:
            upload_s3_file(S3_CODE_BUCKET, file, 'image/jpg')
            print('Uploaded file to S3: {}'.format(join(S3_CODE_BUCKET, file)))

    # Create an instance profile to provide S3 access to the EC2 instance.
    if args.profile or args.all:
        initialize_instance_profile(S3_ROLE_NAME, S3_INSTANCE_PROFILE_NAME)

    # Create a security group to enable SSH access for the EC2 instance.
    if args.security_group or args.all:
        initialize_ssh_security_group(SECURITY_GROUP)
        print('Security group: {}'.format(SECURITY_GROUP))

    # Create an EC2 instance running image.py
    if args.instance or args.all:
        if args.keypair == None:
            print(
                'Creating EC2 instance without an authentication mechanism (use "--keypair")')
        if args.profile or args.all:
            print('Waiting for instance profile to propagate...')
            time.sleep(10)

        instance = initilize_server(SECURITY_GROUP, args.keypair)
        print('Initialized server: {}'.format(instance.id))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Set up Image Thumbnailing Environment')
    parser.add_argument(
        '--keypair', help='Keypair name to use when accessing EC2 instance')

    parser.add_argument('--all', default=False, action='store_true',
                        help='Run all setup steps sequentially')

    parser.add_argument('--queue', default=False, action='store_true',
                        help='Set up the security group for EC2')
    parser.add_argument('--buckets', default=False,
                        action='store_true', help='Setup all S3 buckets')
    parser.add_argument('--upload_code', default=False,
                        action='store_true', help='Upload code files to S3')
    parser.add_argument('--profile', default=False, action='store_true',
                        help='Create the IAM role to give the EC2 instance S3 access')
    parser.add_argument('--security_group', default=False,
                        action='store_true', help='Set up the security group for EC2')
    parser.add_argument('--instance', default=False,
                        action='store_true', help='Launch the EC2 instance')

    args = parser.parse_args()

    setup(args)
