from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.branches import create_branch_f, update_branch_f
from models.branches import Branches
from routes.login import get_current_active_user
from schemas.branches import CreateBranch, UpdateBranch
from schemas.users import CreateUser
from db import database


branches_router = APIRouter(
    prefix="/branches",
    tags=["Branches operation"]
)


@branches_router.get('/get_all')
def get_all(db: Session = Depends(database),
            current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.branch_id != 0:
        raise HTTPException(status_code=400, detail="Sizga ruxsat berilmagan!")
    return db.query(Branches).all()


@branches_router.get('/get_own')
def get_own(db: Session = Depends(database),
            current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Branches).filter(Branches.id == current_user.branch_id).first()


@branches_router.post('/create')
def create_user(form: CreateBranch, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    create_branch_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@branches_router.put("/update")
def update_user(form: UpdateBranch, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    update_branch_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")



