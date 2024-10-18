import io
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from app.s3_manager import S3Manager

app = FastAPI()
s3_manager = S3Manager()

ALLOWED_MAX_SIZE = 10 * 1024 * 1024
ALLOWED_TYPES = ["text/plain"]

# Not a requirement - just to showcase that file validation should be performed
def validate_file(file: UploadFile = File(...)):
    data = file.file.read()
    
    if len(data) > ALLOWED_MAX_SIZE:
        raise HTTPException(status_code=400, detail="File exceeds the maximum allowed size")
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file format")

    # Point back to file beginning
    file.file.seek(0)

@app.post("/upload/")
async def upload_file(bucket_name: str, file_name: str, file: UploadFile = File(...)):
    validate_file(file)
    res = s3_manager.upload_file(file.file, file_name, bucket_name)
    if "error" in res:
        raise HTTPException(status_code=400, detail=res["error"])
    return res

@app.get("/download/")
async def download_file(bucket_name: str, file_name: str):
    file_data = s3_manager.download_file(file_name, bucket_name)
    if isinstance(file_data, dict) and "error" in file_data:
        raise HTTPException(status_code=404, detail=file_data["error"])
    
    return StreamingResponse(io.BytesIO(file_data), media_type="application/octet-stream")