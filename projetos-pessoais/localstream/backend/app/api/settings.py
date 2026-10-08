import os
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.crud import get_setting, set_setting
from app.services.scanner import scan_directory
from app.schemas.settings import SettingsInput

router = APIRouter()

@router.get("/settings")
def read_settings(db: Session = Depends(get_db)):
    directory = get_setting(db, "media_directory")
    return {"media_directory": directory}

@router.post("/settings")
def save_settings(body: SettingsInput, db: Session = Depends(get_db)):
    if not os.path.isdir(body.directory):
        raise HTTPException(status_code=400, detail="Invalid directory path")
    
    set_setting(db, "media_directory", body.directory)
    result = scan_directory(body.directory, db)
    return {
        "message": "Settings updated successfully",
        "media_directory": body.directory,
        "scan": result
        }