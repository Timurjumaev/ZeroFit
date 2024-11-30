from fastapi import APIRouter
from routes.login import login_router
from routes.users import users_router
from routes.branches import branches_router
from routes.tariffs import tariffs_router
from routes.attendances import attendances_router
from routes.clients import clients_router
from routes.sales import sales_router
from routes.transactions import transactions_router
from routes.kassas import kassas_router


api = APIRouter()


api.include_router(login_router)
api.include_router(branches_router)
api.include_router(users_router)
api.include_router(kassas_router)
api.include_router(tariffs_router)
api.include_router(clients_router)
api.include_router(sales_router)
api.include_router(attendances_router)
api.include_router(transactions_router)
