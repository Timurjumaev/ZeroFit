from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.kassas import Kassas
from utils.db_operations import save_in_db
from routes.login import get_current_active_user
from schemas.users import CreateUser
from db import database


kassas_router = APIRouter(
    prefix="/kassas",
    tags=["Kassas operation"]
)


@kassas_router.get('/get')
def get_tariff(db: Session = Depends(database),
               current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Kassas).filter(Kassas.branch_id == current_user.branch_id).first()


@kassas_router.post('/create')
def create_user(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    if db.query(Kassas).filter(Kassas.branch_id == current_user.branch_id).first():
        raise HTTPException(status_code=400, detail="Kassa allaqachon mavjud!")
    new_item_db = Kassas(
        balance=0,
        branch_id=current_user.branch_id
    )
    save_in_db(db, new_item_db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")






