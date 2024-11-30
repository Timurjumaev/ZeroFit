from models.tariffs import Tariffs


def update_tariff_f(the_user, form, db):
    db.query(Tariffs).filter(Tariffs.branch_id == the_user.branch_id).update({
        Tariffs.daily: form.daily,
        Tariffs.monthly: form.monthly,
        Tariffs.three_monthly: form.three_monthly,
        Tariffs.six_monthly: form.six_monthly,
        Tariffs.yearly: form.yearly
    })
    db.commit()



