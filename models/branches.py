from db import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, func, text


class Branches(Base):
    __tablename__ = 'branches'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=func.now() + text("INTERVAL 5 HOUR"))

