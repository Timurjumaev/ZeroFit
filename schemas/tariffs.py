from pydantic import BaseModel, Field


class CreateTariff(BaseModel):
    daily: int = Field(..., gt=0)
    monthly: int = Field(..., gt=0)
    three_monthly: int = Field(..., gt=0)
    six_monthly: int = Field(..., gt=0)
    yearly: int = Field(..., gt=0)



