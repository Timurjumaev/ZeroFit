from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.tariffs import update_tariff_f
from models.tariffs import Tariffs
from routes.login import get_current_active_user
from schemas.tariffs import CreateTariff
from schemas.users import CreateUser
from db import database


tariffs_router = APIRouter(
    prefix="/tariffs",
    tags=["Tariffs operation"]
)


@tariffs_router.get('/get')
def get_tariff(db: Session = Depends(database),
               current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Tariffs).filter(Tariffs.branch_id == current_user.branch_id).first()


@tariffs_router.put("/update")
def update_user(form: CreateTariff, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    update_tariff_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")



