import os
from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import StreamingResponse, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.crud import get_media_by_id
from app.config import CHUNK_SIZE

router = APIRouter()

CONTENT_TYPES = {
    "mp4": "video/mp4",
    "mkv": "video/x-matroska",
    "avi": "video/x-msvideo",
    "mov": "video/quicktime",
    ".m4v": "video/mp4",
}

def file_iterator(file_path: str, start: int, end: int):
    with open(file_path, "rb") as f:
        f.seek(start)
        remaining = end - start + 1
        while remaining > 0:
            chunk = f.read(min(CHUNK_SIZE, remaining))
            if not chunk:
                break
            remaining -= len(chunk)
            yield chunk

@router.get("/stream/{media_id}")
def stream_media(media_id: int, request: Request, db: Session = Depends(get_db)):
    media = get_media_by_id(db, media_id)
    if not media:
        raise HTTPException(status_code=404, detail="Media not found")
    
    file_path = media.file_path
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    file_size = os.path.getsize(file_path)
    ext = os.path.splitext(file_path)[1].lower()
    content_type = CONTENT_TYPES.get(ext, "video/mp4")

    range_header = request.headers.get("Range")

    if not range_header:
        return StreamingResponse(
            file_iterator(file_path, 0, file_size - 1), 
            media_type=content_type,
            headers={"Accept-Ranges": "bytes"}
        )
    
    range_value = range_header.strip().replace("bytes=", "")
    start_str, _, end_str = range_value.partition("-")
    start = int(start_str)
    end = int(end_str) if end_str else file_size - 1

    if start >= file_size or end >= file_size:
        raise HTTPException(status_code=416, detail="Requested range not satisfiable")
    
    headers = {
        "Content-Range": f"bytes {start}-{end}/{file_size}",
        "Accept-Ranges": "bytes",
        "Content-Length": str(end - start + 1),
        "Content-Type": content_type,
    }

    return StreamingResponse(
        file_iterator(file_path, start, end),
        status_code=206,
        headers=headers,
        media_type=content_type,
    )