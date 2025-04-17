from typing import List
from fastapi import APIRouter, Depends
from app.db import get_session
from schemas.user import UserCreate
from sqlmodel import Session, select
from models.user import User
from models.budget import Budget
from schemas.user import UserRead
import uuid
from datetime import datetime

router = APIRouter()

@router.get('/', response_model=List[UserRead])
async def get_users(session: Session=Depends(get_session)):
    all_users = session.exec(select(User)).all()
    return all_users

@router.post('/')
async def create_user(user_create: UserCreate, session: Session=Depends(get_session)):
    # check for existing user
    existing_user = session.exec(
        select(User).where(User.email == user_create.email)).first()
    if existing_user:
        return {"error": "Error: User already exists with this email"}
    # create user
    user = User(
        id=str(uuid.uuid4()),
        username=user_create.username,
        email=user_create.email,
        created_at=datetime.utcnow(),
    )

    user.set_password(user_create.password)

    session.add(user)
    session.commit()
    session.refresh(user)

    return user