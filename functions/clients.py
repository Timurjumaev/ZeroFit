from sqlalchemy.orm import joinedload
from utils.db_operations import get_in_db, save_in_db
from models.clients import Clients
from models.sales import Sales
from fastapi.exceptions import HTTPException
import math


def get_clients(usr, is_active, search, page, limit, db):
    clients_number = db.query(Clients).filter(Clients.branch_id == usr.branch_id).count()
    if is_active is None:
        is_active_filter = Clients.id > 0
    elif is_active:
        is_active_filter = Clients.is_active == True
    else:
        is_active_filter = Clients.is_active == False

    if search:
        search_formatted = "%{}%".format(search)
        search_filter = (Clients.name.like(search_formatted) |
                         Clients.surname.like(search_formatted) |
                         Clients.phone.like(search_formatted))
    else:
        search_filter = Clients.id > 0

    form = (db.query(Clients)
            .options(joinedload(Clients.attendances),
                     joinedload(Clients.sales).options(joinedload(Sales.transactions)))\
            .filter(Clients.branch_id == usr.branch_id, is_active_filter, search_filter).order_by(Clients.name))

    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak")
    elif page and limit:
        return {"clients_number": clients_number, "current_page": page, "limit": limit, "pages": math.ceil(form.count() / limit),
                "data": form.offset((page - 1) * limit).limit(limit).all()}
    else:
        return {"data": form.all()}


def create_client_f(the_user, form, db):
    new_item_db = Clients(
        name=form.name,
        surname=form.surname,
        phone=form.phone,
        branch_id=the_user.branch_id
        )
    save_in_db(db, new_item_db)


def update_client_f(the_user, form, db):
    the_client = get_in_db(db, Clients, form.id)
    if the_client.branch_id != the_user.branch_id:
        raise HTTPException(status_code=400, detail="Mijoz sizning filialingizga tegishli emas!")
    db.query(Clients).filter(Clients.id == form.id).update({
        Clients.name: form.name,
        Clients.surname: form.surname,
        Clients.phone: form.phone,
    })
    db.commit()


def delete_client_f(usr, ident, db):
    cl = get_in_db(db, Clients, ident)
    if cl.branch_id != usr.branch_id:
        raise HTTPException(status_code=400, detail="Mijoz sizning filialingizga tegishli emas!")
    db.query(Clients).filter(Clients.id == ident).delete()
    db.commit()

