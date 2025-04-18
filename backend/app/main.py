# config
from fastapi import FastAPI
from sqlmodel import SQLModel, Session, create_engine
import os

# routes
from routes.post.index import router as index_router
from routes.post.user import router as users_router
from routes.post.budget import router as budgets_router

app = FastAPI()

# call routers
app.include_router(index_router)
app.include_router(users_router, prefix='/users')
app.include_router(budgets_router, prefix='/budgets')