from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from schemas.budget import BudgetRead
from models.budget import Budget
from app.db import get_session

router = APIRouter()

@router.get('/', response_model=List[BudgetRead])
async def getBudgets(session: Session=Depends(get_session)):
    all_budgets = session.exec(select(Budget)).all()
    return all_budgets