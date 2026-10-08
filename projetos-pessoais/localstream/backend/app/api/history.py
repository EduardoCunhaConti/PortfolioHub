from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.database import get_db
from app.db.crud import get_media_by_id, create_or_update_history, get_history_by_media_id

router = APIRouter()

class HistoryInput(BaseModel):
    media_id: int
    progress: int

@router.post("/history")
def save_history(body: HistoryInput, db: Session = Depends(get_db)):
    media = get_media_by_id(db, body.media_id)
    if not media:
        raise HTTPException(status_code=404, detail="Media not found")

    history = create_or_update_history(db, body.media_id, body.progress)
    return {
        "message": "History saved successfully",
        "media_id": history.media_id,
        "progress": history.progress
        }

@router.get("/history/{media_id}")
def get_history(media_id: int, db: Session = Depends(get_db)):
    history = get_history_by_media_id(db, media_id)
    return {
        "media_id": media_id,
        "progress": history.progress if history else 0
    }