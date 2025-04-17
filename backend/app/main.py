# config
from fastapi import FastAPI
from sqlmodel import SQLModel, Session, create_engine
import os

# routes
from routes.post.user import router as users_router

app = FastAPI()

# call routers
app.include_router(users_router, prefix='/users')