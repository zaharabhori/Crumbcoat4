# In website/storage_backends.py

import boto3
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from datetime import timedelta

class S3PrivateMediaStorage(S3Boto3Storage):
    """
    Custom storage backend to provide signed URLs for private files.
    """
    def get_s3_signed_url(self, name):
        """
        Generate a signed URL for private media files.
        """
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': name},
            ExpiresIn=3600  # Expiry time in seconds (1 hour)
        )
        return url
