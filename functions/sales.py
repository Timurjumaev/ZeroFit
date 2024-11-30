from models.clients import Clients
from utils.db_operations import get_in_db, save_in_db
from models.sales import Sales
from models.transactions import Transactions
from models.kassas import Kassas
from models.tariffs import Tariffs
from fastapi.exceptions import HTTPException


def create_sale_f(the_user, form, db):
    get_in_db(db, Clients, form.client_id)
    new_item_db = Sales(
        type=form.type,
        name=form.name,
        money=form.money,
        tariff=form.tariff,
        start_date=form.start_date,
        end_date=form.end_date,
        status=form.status,
        client_id=form.client_id,
        branch_id=the_user.branch_id
        )
    save_in_db(db, new_item_db)
    if form.type == "bar" and form.status:
        new_tr_db = Transactions(
            type="income",
            sale_id=new_item_db.id,
            money=form.money,
            branch_id=the_user.branch_id
        )
        save_in_db(db, new_tr_db)
    elif form.type == "tariff":
        if db.query(Tariffs).filter(Tariffs.id > 0).first() is None:
            raise HTTPException(status_code=400, detail="Tarif topilmadi!")
        if form.tariff == "daily":
            money = db.query(Tariffs).filter(Tariffs.id > 0).first().daily
        elif form.tariff == "monthly":
            money = db.query(Tariffs).filter(Tariffs.id > 0).first().monthly
        elif form.tariff == "three_monthly":
            money = db.query(Tariffs).filter(Tariffs.id > 0).first().three_monthly
        elif form.tariff == "six_monthly":
            money = db.query(Tariffs).filter(Tariffs.id > 0).first().six_monthly
        else:
            money = db.query(Tariffs).filter(Tariffs.id > 0).first().yearly
        db.query(Clients).filter(Clients.id == form.client_id).update({
            Clients.is_allowed: True,
            Clients.until_date: form.end_date
        })
        db.commit()
        new_tr_db = Transactions(
            type="income",
            sale_id=new_item_db.id,
            money=money,
            branch_id=the_user.branch_id
        )
        save_in_db(db, new_tr_db)
        db.query(Kassas).filter(Kassas.id > 0).update({
            Kassas.balance: Kassas.balance + new_tr_db.money
        })
        db.commit()


def confirmation_sale_f(the_user, form, db):
    for ident in form.idents:
        sale = get_in_db(db, Sales, ident)
        if sale.status:
            raise HTTPException(status_code=400, detail="Tanlangan savdo allaqachon yakunlangan!")
        else:
            db.query(Sales).filter(Sales.id == ident).update({
                Sales.status: True
            })
            db.commit()
            new_tr_db = Transactions(
                type="income",
                sale_id=ident,
                money=sale.money,
                branch_id=the_user.branch_id
            )
            save_in_db(db, new_tr_db)
            db.query(Kassas).filter(Kassas.id > 0).update({
                Kassas.balance: Kassas.balance + new_tr_db.money
            })
            db.commit()


