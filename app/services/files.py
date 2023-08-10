import uuid
import os
# AWS S3
import boto3
# Settings
from app.core.settings import settings
# FastAPI
import fastapi
from fastapi import UploadFile
from fastapi.exceptions import HTTPException

status = fastapi.status

# AWS
s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY,
)
bucket = settings.AWS_BUCKET

class TmpFile():
    filename: str
    path: str

    def __init__(self, key: str):
        if os.path.exists('/tmp/files') is False:
            os.mkdir('/tmp/files')
        # Set
        splited = key.split('/')
        self.filename = splited[len(splited) - 1]
        # Path
        self.path = f'/tmp/files/{uuid.uuid4().hex}_{key}'
        print(self.path)

        s3_client.download_file(bucket, key, self.path)

    def get_path(self):
        return self.path
    
    def get_filename(self):
        return self.filename

    def remove_file(self):
        os.unlink(self.path)

class Files():
    def upload_file(self, key: str, file: UploadFile) -> str:
        try:
            file.file.seek(0)
            s3_client.upload_fileobj(file.file, bucket, key)
            return key
        except:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail='No se pudo subir el archivo',
            )
        finally:
            file.file.close()

    def get_file(self, key: str):
        return TmpFile(key)

files_service = Files()
