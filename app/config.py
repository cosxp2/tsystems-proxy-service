import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_ACCESS = os.getenv("AWS_SECRET_ACCESS")
    AWS_REGION = os.getenv("AWS_REGION")