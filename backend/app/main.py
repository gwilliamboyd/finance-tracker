# config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session, create_engine
import os

# routes
from routes.post.index import router as index_router
from routes.post.user import router as users_router
from routes.post.budget import router as budgets_router

app = FastAPI()

# middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# call routers
app.include_router(index_router)
app.include_router(users_router, prefix='/users')
app.include_router(budgets_router, prefix='/budgets')