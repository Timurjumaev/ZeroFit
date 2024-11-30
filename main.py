from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import api
from fastapi.staticfiles import StaticFiles
import os.path

description = """
------------------------------
**Username and password for ZeroFitAdmin**
* Login: **zerofitadmin**
* Parol: **zerofit0**
------------------------------
"""

app = FastAPI(
    description=description,
    contact={
        'name': "Temur Jumayev's telegram account url for questions",
        'url': 'https://t.me/Temur_Jumayev',
    },
    docs_url='/',
    redoc_url='/redoc',
)

app.include_router(api)


@app.get('/files/{fileName}')
async def get_file(fileName: str):
    path = f"./files/{fileName}"
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(400, "Not Found")
#
#
# @app.get('/adminer')
# async def read_php_file():
#     with open("adminer.php", "r") as php_file:
#         php_code = php_file.read()
#
#     return HTMLResponse(content=php_code)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], )




