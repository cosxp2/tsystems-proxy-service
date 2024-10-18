import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from app.config import Config

class S3Manager: 
    def __init__(self):
        self.s3_client = boto3.client(
            "s3", 
            aws_access_key_id=Config.AWS_ACCESS_KEY, 
            aws_secret_access_key=Config.AWS_SECRET_ACCESS, 
            region_name=Config.AWS_REGION
        )
        
    def upload_file(self, file, file_name, bucket_name):
        try:
            self.s3_client.upload_fileobj(Fileobj=file, Bucket=bucket_name, Key=file_name)
            return {"message": "File uploaded succsessfully"}
        except NoCredentialsError:
            return {"error": "Invalid credentials"}
        except ClientError as e:
            return {"error": str(e)}
    
    def download_file(self, file_name, bucket_name):
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=file_name)
            print("success")
            return response["Body"].read()
        except NoCredentialsError:
            return {"error": "Invalid credentials"}
        except ClientError as e:
            return {"error": str(e)}