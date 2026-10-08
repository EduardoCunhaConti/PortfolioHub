from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    file_path = Column(Text, nullable=False, unique=True)
    media_type = Column(Text, nullable=False) #movie or series
    duration = Column(Integer, nullable=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    history = relationship("WatchHistory", back_populates="media")

class WatchHistory(Base):
    __tablename__ = 'watch_history'

    id = Column(Integer, primary_key=True)
    media_id = Column(Integer, ForeignKey('media.id'), nullable=False)
    watched_at = Column(DateTime, default=datetime.utcnow)
    progress = Column(Integer, default=0)

    media = relationship("Media", back_populates="history")

class Settings(Base):
    __tablename__ = 'settings'

    key = Column(Text, primary_key=True)
    value = Column(Text, nullable=False)