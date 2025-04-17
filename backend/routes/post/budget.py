from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from schemas.budget import BudgetRead, BudgetCreate
from models.budget import Budget
from app.db import get_session
import uuid
from datetime import datetime

router = APIRouter()

@router.get('/', response_model=List[BudgetRead])
async def getBudgets(session: Session=Depends(get_session)):
    all_budgets = session.exec(select(Budget)).all()
    return all_budgets

@router.post('/')
async def createBudget(budget_create: BudgetCreate, session: Session=Depends(get_session)):
    existing_budget = session.exec(
        select(Budget).where(Budget.name == budget_create.name)
    ).first()

    if existing_budget:
        return {"error": "Error: Budget already exists."}
    
    budget = Budget(
        id=str(uuid.uuid4()),
        name=budget_create.name,
        amount=budget_create.amount,
        created_at=datetime.utcnow(),
        user_id=budget_create.user_id
    )

    session.add(budget)
    session.commit()
    session.refresh(budget)

    return budget