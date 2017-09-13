"""CMSC389L: Codelab 2"""
import argparse
import boto3
import os


def upload(path, bucket, acl='private', s3_dest=''):
	"""CLI tool to upload files or directories into S3.

	Args:
		path (string): Path to file on local system.
		bucket (string): S3 bucket name.
		acl (string): Optional ACL to set on this object.
		s3_dest (string): Destination name of uploaded content.
	"""
	pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Uploads files/directories to S3.")
	parser.add_argument('path', help='file path to file or directory to upload')
	parser.add_argument('--bucket', required=True, help='S3 bucket to upload into')
	parser.add_argument('--destination', default='', help='name to use for uploaded file or directory')
	parser.add_argument('--acl', default='', help='canned acl to attach to all uploaded objects', choices=['private', 'public-read'])

	args = parser.parse_args()

	path = os.path.normpath(args.path)

	upload(path, args.bucket, args.acl, args.destination)
