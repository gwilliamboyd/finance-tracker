from sqlmodel import SQLModel
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserRead(SQLModel):
    id: str
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

class UserResponse(UserRead):
    class Config:
        orm_mode = True

