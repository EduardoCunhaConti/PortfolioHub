from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MediaOut(BaseModel):
    id: int
    title: str
    media_type: str
    duration: Optional[int] = None
    added_at: datetime
    progress: Optional[int] = 0

    class Config:
        from_attributes = True