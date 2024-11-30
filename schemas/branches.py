from pydantic import BaseModel, Field


class CreateBranch(BaseModel):
    name: str
    status: bool


class UpdateBranch(BaseModel):
    id: int = Field(..., gt=0)
    name: str
    status: bool


