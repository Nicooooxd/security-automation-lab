from pydantic import BaseModel


class SecurityEvent(BaseModel):
    username: str
    ip: str
    action: str
    success: bool