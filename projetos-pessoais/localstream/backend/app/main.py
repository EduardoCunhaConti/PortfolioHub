from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.db.database import create_tables
from app.api import media, stream, history, settings
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(title="LocalStream")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(media.router, prefix="/api")
app.include_router(stream.router, prefix="/api")
app.include_router(history.router, prefix="/api")
app.include_router(settings.router, prefix="/api")

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "frontend")

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/player")
def serve_player():
    return FileResponse(os.path.join(FRONTEND_DIR, "player.html"))

@app.get("/settings")
def serve_settings():
    return FileResponse(os.path.join(FRONTEND_DIR, "settings.html"))

@app.on_event("startup")
def on_startup():
    create_tables()