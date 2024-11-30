from models.kassas import Kassas
from models.tariffs import Tariffs
from utils.db_operations import get_in_db, save_in_db
from models.branches import Branches
from fastapi.exceptions import HTTPException


def create_branch_f(the_user, form, db):
    if the_user.branch_id != 0:
        raise HTTPException(status_code=400, detail="Sizga ruxsat berilmagan!")
    new_item_db = Branches(
        name=form.name,
        status=form.status)
    save_in_db(db, new_item_db)
    new_tariff_db = Tariffs(
        daily=0,
        monthly=0,
        three_monthly=0,
        six_monthly=0,
        yearly=0,
        branch_id=new_item_db.id,
    )
    save_in_db(db, new_tariff_db)
    new_item_db = Kassas(
        balance=0,
        branch_id=new_item_db.id
    )
    save_in_db(db, new_item_db)


def update_branch_f(the_user, form, db):
    if the_user.branch_id != 0:
        raise HTTPException(status_code=400, detail="Sizga ruxsat berilmagan!")
    get_in_db(db, Branches, form.id)
    db.query(Branches).filter(Branches.id == form.id).update({
        Branches.name: form.name,
        Branches.status: form.status
    })
    db.commit()



