from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.attendances import create_attendance_f
from routes.login import get_current_active_user
from schemas.attendances import CreateAttendance
from schemas.users import CreateUser
from db import database


attendances_router = APIRouter(
    prefix="/attendances",
    tags=["Attendances operation"]
)


@attendances_router.post('/create')
def create_user(form: CreateAttendance, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    create_attendance_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")