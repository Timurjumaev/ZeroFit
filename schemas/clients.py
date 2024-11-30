from pydantic import BaseModel, Field


class CreateClient(BaseModel):
    name: str
    surname: str
    phone: str


class UpdateClient(BaseModel):
    id: int = Field(..., gt=0)
    name: str
    surname: str
    phone: str

