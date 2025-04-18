from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def getIndex():
    return 'Welcome to G\'s Finance Tracker Server. Please visit \'/users/\' or \'/budgets/\' to view info!'
