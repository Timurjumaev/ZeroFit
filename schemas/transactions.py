from pydantic import BaseModel


class CreateTransaction(BaseModel):
    money: int
    comment: str




