import enum
import boto3
from botocore import endpoint
from botocore.exceptions import ClientError, NoRegionError
from fastapi.param_functions import Body
from config import config
from fastapi import HTTPException, status
import logging
import io


def get_client():
    try:
        return boto3.client(
            "s3",
            endpoint_url="http://{}:{}".format(
                config["MINIO_ADDRESS"], config["MINIO_PORT"]
            ),
            aws_access_key_id=config["MINIO_ACCESS_KEY"],
            aws_secret_access_key=config["MINIO_SECRET_KEY"],
        )
    except ClientError as e:
        print("[INFO] Error when connect to minio storage")
        logging.error(e)
        return None


def save_images(images, folder_name):
    s3_client = get_client()
    if s3_client is None:
        return False
    try:
        for i, buffer in enumerate(images):
            s3_client.put_object(
                Bucket=config["BUCKET_IMAGE"],
                Key="images/{}/{}".format(folder_name, i),
                Body=buffer,
                ContentType="image/png",
            )
        return True
    except ClientError as e:
        logging.error(e)
        return None
