import logging
import boto3
from botocore.exceptions import ClientError
from settings import LOGGING, AWS_S3_BUCKET_NAME


logger = logging.getLogger('*')


def upload_to_bucket(file_path, filename):
    """
    Upload file to S3 bucket
    """
    s3_client = boto3.client('s3')
    success = False
    try:
        response = s3_client.upload_file(file_path, AWS_S3_BUCKET_NAME, filename)
        success = True
    except ClientError as e:
        logger.error('Error at %s', 'boto3.exceptions.ClientError', exc_info=e)
    return success
