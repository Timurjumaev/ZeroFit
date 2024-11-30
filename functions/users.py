from routes.login import get_password_hash
from utils.db_operations import get_in_db, save_in_db
from models.users import Users
from fastapi.exceptions import HTTPException


def create_user_f(the_user, form, db):
    if the_user.branch_id != 0:
        raise HTTPException(status_code=400, detail="Sizga ruxsat berilmagan!")
    new_item_db = Users(
        username=form.username,
        password=get_password_hash(form.password),
        preferred_language=form.preferred_language,
        branch_id=form.branch_id)
    save_in_db(db, new_item_db)


def update_user_f(the_user, form, db):
    usr = get_in_db(db, Users, form.id)
    if the_user.branch_id != 0 and the_user.id != form.id:
        raise HTTPException(status_code=400, detail="Sizga ruxsat berilmagan!")
    if form.status:
        password = get_password_hash(form.password)
    else:
        password = usr.password

    db.query(Users).filter(Users.id == form.id).update({
        Users.username: form.username,
        Users.password: password,
        Users.preferred_language: form.preferred_language,
    })
    db.commit()



