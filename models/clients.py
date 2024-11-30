from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, String, Integer, DateTime, func, Boolean, Date, text
from models.attendances import Attendances


class Clients(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=True)
    phone = Column(String(255), nullable=True)
    is_active = Column(Boolean, nullable=False, default=False)
    is_allowed = Column(Boolean, nullable=False, default=False)
    until_date = Column(Date, default=None)
    created_at = Column(DateTime, default=func.now() + text("INTERVAL 5 HOUR"))
    branch_id = Column(Integer, nullable=False)

    attendances = relationship(Attendances, order_by=Attendances.date.desc())

