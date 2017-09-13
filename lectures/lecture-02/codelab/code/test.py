"""CMSC389L: Codelab 2"""
import boto3
import requests
import unittest
import uuid

from upload import upload

test_bucket = "test-bucket-{}".format(uuid.uuid4())

def setUpModule():
    # Initialize a bucket for testing.
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=test_bucket)

def tearDownModule():
    # Clean up the bucket and any objects.
    bucket = boto3.resource('s3').Bucket(test_bucket)
    bucket.objects.all().delete()
    bucket.delete()

def read(key):
    """Reads a key from the test bucket and returns its data as a string."""
    obj = boto3.resource('s3').Object(test_bucket, key)
    return obj.get()['Body'].read().decode('utf-8')

def load(localpath, s3_path):
    data = read(s3_path)
    with open(localpath, 'r') as f:
        return data, f.read()

class TestUploadFile(unittest.TestCase):
    def test_upload_file(self):
        """Test that uploading a file yields the correct data."""
        upload('test.py', test_bucket)
        self.assertEquals(*load('test.py', 'test.py'))
        

    def test_upload_file_prefix(self):
        """Test uploading a file into an S3 directory."""
        upload('test.py', test_bucket, s3_dest='foo/bar.txt')
        self.assertEquals(*load('test.py', 'foo/bar.txt'))

    def test_upload_file_private(self):
        """Test that objects uploaded with a private ACL are inaccessible to the public."""
        upload('test.py', test_bucket, acl='private', s3_dest='foo/bar.txt')
        s3_url = 'https://s3.amazonaws.com/{}/foo/bar.txt'.format(test_bucket)
        r = requests.get(s3_url)
        self.assertEquals(r.status_code, 403)
        self.assertIn('<Message>Access Denied</Message>', r.text)

    def test_upload_file_public(self):
        """Test that objects uploaded with a public ACL are accessible to the public."""
        upload('test.py', test_bucket, acl='public-read', s3_dest='foo/bar.txt')
        s3_url = 'https://s3.amazonaws.com/{}/foo/bar.txt'.format(test_bucket)
        r = requests.get(s3_url)
        self.assertEquals(r.status_code, 200)


class TestUploadDirectory(unittest.TestCase):
    def test_upload_directory(self):
        """Test that uploading a directory uploads all of its files."""
        upload('test-dir', test_bucket)
        self.assertEquals(*load('test-dir/test-file.txt', 'test-file.txt'))
        self.assertEquals(*load('test-dir/test-sub-dir/test-file-2.txt', 'test-sub-dir/test-file-2.txt'))

    def test_upload_directory_dest(self):
        """Test that uploading a directory uploads all of its files into the specified S3 destination."""
        upload('test-dir', test_bucket, s3_dest='uploads')
        self.assertEquals(*load('test-dir/test-file.txt', 'uploads/test-file.txt'))
        self.assertEquals(*load('test-dir/test-sub-dir/test-file-2.txt', 'uploads/test-sub-dir/test-file-2.txt'))

    def test_upload_directory_private(self):
        """Test that objects uploaded with a private ACL are inaccessible to the public."""
        upload('test-dir', test_bucket, acl='private', s3_dest='uploads')
        s3_url = 'https://s3.amazonaws.com/{}/uploads/test-file.txt'.format(test_bucket)
        r = requests.get(s3_url)
        self.assertEquals(r.status_code, 403)
        self.assertIn('<Message>Access Denied</Message>', r.text)

    def test_upload_directory_public(self):
        """Test that objects uploaded with a public ACL are accessible to the public."""
        upload('test-dir', test_bucket, acl='public-read', s3_dest='uploads')
        s3_url = 'https://s3.amazonaws.com/{}/uploads/test-file.txt'.format(test_bucket)
        r = requests.get(s3_url)
        self.assertEquals(r.status_code, 200)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
