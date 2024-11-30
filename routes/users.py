from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.users import create_user_f, update_user_f
from models.users import Users
from routes.login import get_current_active_user
from schemas.users import CreateUser, UpdateUser
from db import database


users_router = APIRouter(
    prefix="/users",
    tags=["Users operation"]
)


@users_router.get('/get')
def get(current_user: CreateUser = Depends(get_current_active_user)):
    return current_user


@users_router.get('/get_all')
def get(branch_id: int = None, db: Session = Depends(database), current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.branch_id != 0:
        raise HTTPException(status_code=400, detail="You are not allowed")
    if branch_id:
        return db.query(Users).filter(Users.branch_id == branch_id).all()
    return db.query(Users).all()


@users_router.post('/create')
def create_user(form: CreateUser, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    create_user_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.put("/update")
def update_user(form: UpdateUser, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    update_user_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")



