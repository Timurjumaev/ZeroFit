from db import Base
from sqlalchemy import Column, Integer


class Tariffs(Base):
    __tablename__ = 'tariffs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    daily = Column(Integer, nullable=False)
    monthly = Column(Integer, nullable=False)
    three_monthly = Column(Integer, nullable=True)
    six_monthly = Column(Integer, nullable=True)
    yearly = Column(Integer, nullable=True)
    branch_id = Column(Integer, nullable=False)
