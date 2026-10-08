from sqlalchemy.orm import Session
from app.db.models import Media, WatchHistory, Settings
from datetime import datetime

# ── Media ──────────────────────────────────────────────────────────────────────
def get_all_media(db: Session):
    return db.query(Media).all()

def get_media_by_id(db: Session, media_id: int):
    return db.query(Media).filter(Media.id == media_id).first()

def get_media_by_path(db: Session, file_path: str):
    return db.query(Media).filter(Media.file_path == file_path).first()

def create_media(db: Session, title: str, file_path: str, media_type: str, duration: int = None):
    media = Media(
        title=title,
        file_path=file_path,
        media_type=media_type,
        duration=duration
    )
    db.add(media)
    db.commit()
    db.refresh(media)
    return media

def delete_media(db: Session, media_id: int):
    media = get_media_by_id(db, media_id)
    if media:
        db.delete(media)
        db.commit()
    return media

# ── Watch History ──────────────────────────────────────────────────────────────────────
def create_or_update_history(db: Session, media_id: int, progress: int):
    history = db.query(WatchHistory).filter(WatchHistory.media_id == media_id).first()
    if history:
        history.progress = progress
        history.watched_at = datetime.utcnow()
        db.commit()
        db.refresh(history)
    else:
        history = WatchHistory(media_id=media_id, progress=progress)
        db.add(history)
        db.commit()
        db.refresh(history)
    return history

def get_history_by_media_id(db: Session, media_id: int):
    return db.query(WatchHistory).filter(WatchHistory.media_id == media_id).first()

# ── Settings ──────────────────────────────────────────────────────────────────────
def get_setting(db: Session, key: str):
   setting = db.query(Settings).filter(Settings.key == key).first()
   return setting.value if setting else None

def set_setting(db: Session, key: str, value: str):
    setting = db.query(Settings).filter(Settings.key == key).first()
    if setting:
        setting.value = value
    else:
        setting = Settings(key=key, value=value)
        db.add(setting)
    db.commit()
    return setting