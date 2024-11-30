from enum import Enum
from pydantic import BaseModel, validator, Field
from db import SessionLocal
from models.users import Users
from utils.db_operations import get_in_db

db = SessionLocal()


class LanguageType(str, Enum):
    lat = "lat"
    cyr = "cyr"
    ru = "ru"


class CreateUser(BaseModel):
    username: str
    password: str
    preferred_language: LanguageType
    branch_id: int = Field(..., gt=0)

    @validator('username')
    def username_validate(cls, username):
        validate_my = db.query(Users).filter(
            Users.username == username,
        ).count()

        if validate_my != 0:
            raise ValueError('Bunday login avval ro`yxatga olingan!')
        return username

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password


class UpdateUser(BaseModel):
    id: int = Field(..., gt=0)
    username: str
    password: str
    preferred_language: LanguageType
    status: bool

    @validator('username')
    def username_validate(cls, username, values):
        if 'id' not in values:
            raise ValueError('ID qiymati mavjud emas!')
        validate_my = db.query(Users).filter(
            Users.username == username,
        ).count()

        the_user = get_in_db(db, Users, values['id'])

        if validate_my != 0 and username != the_user.username:
            raise ValueError('Bunday login avval ro`yxatga olingan!')
        return username

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password

