from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Form
from sqlmodel import Session, select
from models.user import User
from auth.jwt import create_access_token
from app.db import engine

router = APIRouter()

@router.post('/')
def login(username: str = Form(...), password: str = Form(...)):
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.username == username )
            ).first()
        if not user or not user.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials.')
        access_token = create_access_token(data={'sub': user.username})
        return {'access_token': access_token, 'token_type': 'bearer'}
