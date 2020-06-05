from io import BytesIO
from typing import NamedTuple

import boto3
from PIL import Image

S3 = boto3.client('s3')


class S3File(NamedTuple):
    bucket: str
    key: str


def lambda_handler(event, context):
    assert context

    files = get_files(event)
    for s3_file in files:
        resize(s3_file)


def get_files(event: dict):
    for record in event["Records"]:
        s3 = record['s3']
        bucket = s3["bucket"]["name"]
        key = s3["object"]["key"]

        print(f"processing: {bucket}//{key}")

        if "thumbnail" in key:
            print("skip thumbnail")
            continue

        yield S3File(
            bucket=bucket,
            key=key,
        )


def resize(s3_file: S3File):
    size = (128, 128)
    original = download_image(s3_file)
    image_format = s3_file.key.split(".")[-1].upper()
    if image_format == "JPG":
        image_format = "JPEG"
    image = Image.open(original)
    image.thumbnail(size, Image.ANTIALIAS)
    resized = BytesIO()
    image.save(resized, image_format)
    resized.seek(0)
    new_key = f"{s3_file.key}.thumbnail"
    S3.upload_fileobj(resized, s3_file.bucket, new_key)
    print(f"uploaded to: {s3_file.bucket}//{new_key}")


def download_image(s3_file: S3File):
    image = BytesIO()
    S3.download_fileobj(s3_file.bucket, s3_file.key, image)
    print(f"downloaded: {s3_file}: {image.tell()} bytes")
    image.seek(0)
    return image
