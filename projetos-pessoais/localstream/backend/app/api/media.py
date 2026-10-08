from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.crud import get_all_media, get_media_by_id, delete_media, get_history_by_media_id
from app.schemas.media import MediaOut

router = APIRouter()


@router.get("/media", response_model=list[MediaOut])
def list_media(db: Session = Depends(get_db)):
    media_list = get_all_media(db)
    result = []
    for media in media_list:
        history = get_history_by_media_id(db, media.id)
        media_out = MediaOut.from_orm(media) if hasattr(MediaOut, "from_orm") else MediaOut.model_validate(media)
        media_out.progress = history.progress if history else 0
        result.append(media_out)
    return result


@router.get("/media/{media_id}", response_model=MediaOut)
def get_media(media_id: int, db: Session = Depends(get_db)):
    media = get_media_by_id(db, media_id)
    if not media:
        raise HTTPException(status_code=404, detail="Media not found.")
    history = get_history_by_media_id(db, media.id)
    media_out = MediaOut.model_validate(media)
    media_out.progress = history.progress if history else 0
    return media_out


@router.delete("/media/{media_id}")
def remove_media(media_id: int, db: Session = Depends(get_db)):
    media = get_media_by_id(db, media_id)
    if not media:
        raise HTTPException(status_code=404, detail="Media not found.")
    delete_media(db, media_id)
    return {"message": "Media removed successfully."}