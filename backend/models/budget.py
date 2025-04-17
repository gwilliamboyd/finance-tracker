from sqlmodel import SQLModel, Field, Relationship
from models.user import User
from datetime import datetime
import uuid
from typing import Optional

class Budget(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    name: str = Field(index=True, unique=True)
    amount: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user_id: str = Field(foreign_key='user.id', index=True)
    user: Optional['User'] = Relationship(back_populates='budgets')