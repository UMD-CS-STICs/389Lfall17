
import argparse
import boto3
import json

from os.path import join, basename, splitext
from PIL import Image, ImageOps

from config import SQS_QUEUE_NAME, S3_OUTPUT_BUCKET
from utils import upload_s3_file, download_s3_file

sqs = boto3.resource('sqs')
s3 = boto3.resource('s3')

sqs_client = boto3.client('sqs')


def generate_thumbnail(img_path, height, width, dest):
    """Generates a thumbnail of an image into the dest directory.

    Args:
        img_path (string): Relative directory path containing image to thumbnail.
        height (int): Height in pixels of thumbnail image.
        width (int): width in pixels of thumbnail image.
        dest (string): Relative directory path to output thumbnail.

    Returns:
        The relative path to the generated thumbnail.
    """
    # Generate the new filename of the thumbnailed image.
    filename_no_ext = splitext(basename(img_path))[0]
    filename = '{}-{}x{}.jpg'.format(filename_no_ext, width, height)
    output_path = join(dest, filename)

    # Generate the thumbnail.
    image = Image.open(img_path)
    # Scale the image down to the thumbnail size.
    image = ImageOps.fit(image, (width, height))
    image.save(output_path, 'JPEG')
    print('Generated thumbnail: {}'.format(output_path))

    return output_path


def run(local_originals_dir, local_thumbnails_dir):
    """Generates thumbnails based on received SQS requests and uploads to S3.

    Args:
        local_originals_dir (string): Relative directory path to temporarily store original image files from S3.
        local_thumbnails_dir (string): Relative directory path to temporarily store thumbnail image files before uploading to S3.
    """
    # TODO(you)
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SQS-based Image Thumbnailer')
    parser.add_argument('--tmp', default='./tmp',
                        help='Local temporary directory to store images and thumbnails')

    args = parser.parse_args()

    local_originals_dir = join(args.tmp, 'originals')
    local_thumbnails_dir = join(args.tmp, 'thumbnails')

    run(local_originals_dir, local_thumbnails_dir)
