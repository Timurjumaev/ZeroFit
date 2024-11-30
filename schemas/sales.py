from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional, List


class Type(str, Enum):
    bar = "bar"
    tariff = "tariff"


class TariffType(str, Enum):
    daily = "daily"
    monthly = "monthly"
    three_monthly = "three_monthly"
    six_monthly = "six_monthly"
    yearly = "yearly"


class CreateSale(BaseModel):
    type: Type
    name: Optional[str] = None
    money: Optional[int] = None
    tariff: Optional[TariffType] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    client_id: int
    status: bool


class ConfirmationSale(BaseModel):
    idents: List[int]

