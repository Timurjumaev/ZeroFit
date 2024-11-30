from db import Base
from sqlalchemy import Column, String, Integer, DateTime, func, ForeignKey, text


class Attendances(Base):
    __tablename__ = 'attendances'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False, default=func.now() + text("INTERVAL 5 HOUR"))
    client_id = Column(Integer, ForeignKey('clients.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now() + text("INTERVAL 5 HOUR"))
    branch_id = Column(Integer, nullable=False)
