from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, text, and_
from functions.clients import get_clients, create_client_f, update_client_f, delete_client_f
from models.clients import Clients
from models.sales import Sales
from routes.login import get_current_active_user
from schemas.clients import CreateClient, UpdateClient
from schemas.users import CreateUser
from db import database


clients_router = APIRouter(
    prefix="/clients",
    tags=["Clients operation"]
)


@clients_router.get('/get_one')
def get_one(ident: int = 0,
            db: Session = Depends(database),
            current_user: CreateUser = Depends(get_current_active_user)):
    client = db.query(Clients).filter(Clients.branch_id == current_user.branch_id,
                                      Clients.id == ident).first()
    if client is None:
        raise HTTPException(status_code=400, detail="Client not found")
    db.query(Clients).filter(
        Clients.id == ident,
        and_(Clients.until_date.isnot(None), func.date(func.now() + text("INTERVAL 5 HOUR")) > Clients.until_date)
    ).update({
        Clients.is_allowed: False
    })
    db.commit()

    return (db.query(Clients)
            .options(
        joinedload(Clients.attendances),
        joinedload(Clients.sales).options(joinedload(Sales.transactions))
    )
            .filter(Clients.id == ident)
            .first())


@clients_router.get('/get_all')
def get(is_active: bool = None, search: str = None, page: int = 1, limit: int = 25,
        db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    return get_clients(current_user, is_active, search, page, limit, db)


@clients_router.post('/create')
def create_client(form: CreateClient, db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    create_client_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@clients_router.put("/update")
def update_client(form: UpdateClient, db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    update_client_f(current_user, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@clients_router.delete("/delete")
def delete_client(ident: int, db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    delete_client_f(current_user, ident, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")



