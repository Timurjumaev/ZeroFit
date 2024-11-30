from utils.db_operations import save_in_db
from models.transactions import Transactions
from models.kassas import Kassas
from utils.pagination import pagination


def get_transactions(usr, ident, tr_type, start_date, end_date, page, limit, db):

    if ident > 0:
        ident_filter = Transactions.id == ident
    else:
        ident_filter = Transactions.id > 0

    if tr_type:
        type_filter = Transactions.type == tr_type
    else:
        type_filter = Transactions.id > 0

    if start_date:
        start_date_filter = Transactions.created_at > start_date
    else:
        start_date_filter = Transactions.id > 0

    if end_date:
        end_date_filter = Transactions.created_at < end_date
    else:
        end_date_filter = Transactions.id > 0

    items = db.query(Transactions).filter(Transactions.branch_id == usr.branch_id, ident_filter, type_filter,
                                          start_date_filter, end_date_filter).order_by(Transactions.id.desc())

    return pagination(items, page, limit)


def create_transaction_f(the_user, form, db):
    new_item_db = Transactions(
        type="expense",
        money=form.money,
        comment=form.comment,
        branch_id=the_user.branch_id
        )
    save_in_db(db, new_item_db)
    db.query(Kassas).filter(Kassas.id > 0).update({
        Kassas.balance: Kassas.balance - form.money
    })
    db.commit()
