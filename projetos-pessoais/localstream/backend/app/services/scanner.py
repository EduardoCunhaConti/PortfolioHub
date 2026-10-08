import os
import re
from sqlalchemy.orm import Session
from app.db.crud import get_media_by_path, create_media
from app.config import VIDEO_EXTENSIONS

NOISE_PATTERNS = [
    r"\b(1080p|720p|480p|2160p|4k)\b",
    r"\b(bluray|blu-ray|bdrip|brrip|dvdrip|webrip|web-dl|hdtv)\b",
    r"\b(x264|x265|hevc|avc|xvid|divx)\b",
    r"\b(aac|mp3|dts|ac3|truehd)\b",
    r"\b(extended|theatrical|remastered|proper|repack)\b",
    #r"\b\d{4}\b",  # ano
]

def clean_title(filename: str) -> str:
    name = os.path.splitext(filename)[0]
    name = name.replace(".", " ").replace("_", " ")
    for pattern in NOISE_PATTERNS:
        name = re.sub(pattern, '', name, flags=re.IGNORECASE)
    name = re.sub(r"\s+", " ", name).strip()
    return name

def detect_media_type(filename: str, parent_folder: str) -> str:
    series_pattern = r"S\d{2}E\d{2}|Season\s?\d+|Temporada\s?\d+"
    if re.search(series_pattern, filename, re.IGNORECASE):
        return "series"
    if re.search(series_pattern, parent_folder, re.IGNORECASE):
        return "series"
    return "movie"

def scan_directory(directory: str, db: Session) -> dict:
    found = 0
    added = 0

    for root, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in VIDEO_EXTENSIONS:
                continue

            found += 1
            file_path = os.path.join(root, file)

            if get_media_by_path(db, file_path):
                continue

            parent_folder = os.path.basename(root)
            title = clean_title(file)
            media_type = detect_media_type(file, parent_folder)

            create_media(
                db = db,
                title = title,
                file_path = file_path,
                media_type = media_type
            )
            added += 1
    return {"found": found, "added": added}