from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.transactions import create_transaction_f, get_transactions
from routes.login import get_current_active_user
from schemas.transactions import CreateTransaction
from schemas.users import CreateUser
from db import database


transactions_router = APIRouter(
    prefix="/transactions",
    tags=["Transactions operation"]
)


@transactions_router.get('/get',
                         description="tr_type 'income' yoki 'expense' bo'ladi")
def get(ident: int = 0,
        tr_type: str = None,
        start: datetime = None,
        end: datetime = None,
        page: int = 1,
        limit: int = 25,
        db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    return get_transactions(current_user, ident, tr_type, start, end, page, limit, db)


@transactions_router.post('/create')
def create_user(form: CreateTransaction, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    create_transaction_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")




