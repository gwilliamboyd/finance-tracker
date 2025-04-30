# avoid circular imports
from __future__ import annotations
# python imports
import uuid
from typing import List, TYPE_CHECKING
from datetime import datetime
# sqlmodel imports
from sqlmodel import SQLModel, Field, Relationship
# password hash
from passlib.hash import bcrypt
from passlib.context import CryptContext

if TYPE_CHECKING:
    from models.budget import Budget

class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    budgets: List['Budget'] = Relationship(back_populates='user')

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.hashed_password)
    
    def set_password(self, password: str):
        self.hashed_password = bcrypt.hash(password)

    def get_password_hash(self, password):
        pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        return pwd_context.hash(password)