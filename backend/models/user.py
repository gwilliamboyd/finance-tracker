from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from passlib.hash import bcrypt
import uuid

class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.hashed_password)
    
    def set_password(self, password: str):
        self.hashed_password = bcrypt.hash(password)
