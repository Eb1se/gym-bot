from pydantic import BaseModel
from typing import Optional
from datetime import datetime 

class UserCreate(BaseModel):
    """
    Схема для данных, которые приходят при регистрации.
    """
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None

class UserResponse(BaseModel):
    """
    Схема для данных, которые мы отдаем.
    """
    id: int
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    created_at: datetime
    is_new: bool = False
    class Config:
        from_attributes = True