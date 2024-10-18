import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_ACCESS = os.getenv("AWS_SECRET_ACCESS")
    AWS_REGION = os.getenv("AWS_REGION")
    
    if not AWS_ACCESS_KEY or not AWS_SECRET_ACCESS or not AWS_REGION:
        raise EnvironmentError("One or more required environment variables are missing: "
                               "AWS_ACCESS_KEY, AWS_SECRET_ACCESS, AWS_REGION")