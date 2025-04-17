from sqlmodel import SQLModel
from pydantic import BaseModel
from datetime import datetime
from schemas.budget import BudgetRead
from typing import List

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserRead(SQLModel):
    id: str
    username: str
    email: str
    budgets: List[BudgetRead] = []
    created_at: datetime

    class Config:
        from_attributes = True

class UserResponse(UserRead):
    class Config:
        orm_mode = True

