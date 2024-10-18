# T-Systems Proxy Service 

This project is a FastAPI-based application for uploading and downloading files to and from an AWS S3 bucket.

## Features

- **File Upload to S3**: Upload `.txt` files to an AWS S3 bucket
- **File Download from S3**: Download files from an S3 bucket
- **Docker Support**: The project includes Docker configurations for containerization

## Requirements

- **Python 3.11**
- **Pipenv** 
- **AWS Account** (for S3)
- **Docker** (optional)

## Installation

### Clone the Repository

```bash
    git clone https://github.com/cosxp2/tsystems-proxy-service.git
    cd tsystems-proxy-service
```

### Setup AWS Credentials

```bash
    echo "AWS_ACCESS_KEY=your-access-key-id\nAWS_SECRET_ACCESS=your-secret-key\nAWS_REGION=your-aws-region" > .env
```

### Run locally

```bash
    pipenv install --deploy
    pipenv shell
    uvicorn app.main:app --reload
```

### Run in Docker

```bash
    cd docker
    docker compose build
    docker compose up
```

## API Endpoints

### 1. Upload File

**POST** `/upload/`

- **Request Parameters**:
  - `bucket_name` (str): Name of the S3 bucket
  - `file_name` (str): Desired file name in S3
  - `file`: The file to be uploaded

**Request Example (using curl)**:

```bash
    echo "S3 bucket file" > /tmp/testfile.txt
    curl -X POST "http://localhost:8000/upload/?bucket_name=your-bucket&file_name=testfile.txt" \
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@/tmp/testfile.txt"
```
**Response Example**:

```json
    {"message": "File uploaded successfully"}
```

### 2. Download File

**GET** `/download/`

- **Request Parameters**:
  - `bucket_name` (str): Name of the S3 bucket.
  - `file_name` (str): Name of the file to download.

**Request Example (using curl)**:
```bash
curl -X GET "http://localhost:8000/download/?bucket_name=your-bucket&file_name=testfile.txt" \
-H "accept: application/octet-stream"