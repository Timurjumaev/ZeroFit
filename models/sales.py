from sqlalchemy.orm import relationship, backref
from db import Base
from sqlalchemy import Column, String, Integer, Date, func, DateTime, Boolean, text
from models.clients import Clients


class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
    money = Column(Integer, nullable=True)
    tariff = Column(String(255), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now() + text("INTERVAL 5 HOUR"))
    client_id = Column(Integer, nullable=False)
    branch_id = Column(Integer, nullable=False)

    client = relationship('Clients', foreign_keys=[client_id],
                          primaryjoin=lambda: Clients.id == Sales.client_id,
                          backref=backref("sales"))
