# avoid circular imports
from __future__ import annotations
# python imports
from datetime import datetime
import uuid
from typing import Optional, TYPE_CHECKING
# sqlmodel imports
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.user import User

class Budget(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    name: str = Field(index=True, unique=True)
    amount: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user_id: str = Field(foreign_key='user.id', index=True)
    user: Optional['User'] = Relationship(back_populates='budgets')