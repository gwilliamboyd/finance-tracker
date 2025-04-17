from sqlmodel import SQLModel
from pydantic import BaseModel
from datetime import datetime
from models.user import User
from typing import Optional

class BudgetCreate(BaseModel):
    name: str
    amount: float
    created_at: Optional[datetime] = None
    user_id: str

class BudgetRead(SQLModel):
    id: str
    name: str
    amount: float
    user_id: str
    created_at: datetime

    model_config = {
    "from_attributes": True
}

class BudgetResponse(BudgetRead):
    model_config = {
    "from_attributes": True
}

