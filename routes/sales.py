from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.sales import create_sale_f, confirmation_sale_f
from routes.login import get_current_active_user
from schemas.sales import CreateSale, ConfirmationSale
from schemas.users import CreateUser
from db import database


sales_router = APIRouter(
    prefix="/sales",
    tags=["Sales operation"]
)


@sales_router.post('/create')
def create_sale(form: CreateSale, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    create_sale_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@sales_router.put('/confirmation')
def confirmation_sale(form: ConfirmationSale, db: Session = Depends(database),
                      current_user: CreateUser = Depends(get_current_active_user)):
    confirmation_sale_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")





