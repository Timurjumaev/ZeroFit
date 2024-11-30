from models.attendances import Attendances
from utils.db_operations import get_in_db, save_in_db
from models.clients import Clients


def create_attendance_f(the_user, form, db):
    client = get_in_db(db, Clients, form.client_id)
    if client.is_active:
        type_ = "went"
    else:
        type_ = "came"
    new_item_db = Attendances(
        type=type_,
        client_id=form.client_id,
        branch_id=the_user.branch_id
        )
    save_in_db(db, new_item_db)
    if type_ == "came":
        status = True
    else:
        status = False
    db.query(Clients).filter(Clients.id == form.client_id).update({
        Clients.is_active: status
    })
    db.commit()

