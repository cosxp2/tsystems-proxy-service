from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil 

app = FastAPI()

UPLOAD_DIR = Path("/tmp")

if not UPLOAD_DIR.exists():
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    
@app.post("/upload/")
async def upload_file(file_name: str, file: UploadFile = File(...)):
    file_location = UPLOAD_DIR / file_name
    
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {e}")
    
    return {"message": f"File {file_name} uploaded successfully"}

@app.get("/download/")
async def download_file(file_name: str):
    file_location = UPLOAD_DIR / file_name
    
    if not file_location.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_location, media_type="application/octetstream", filename=file_name)