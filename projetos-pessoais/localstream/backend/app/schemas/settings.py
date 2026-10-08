from pydantic import BaseModel

class SettingsInput(BaseModel):
    directory: str