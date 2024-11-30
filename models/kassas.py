from db import Base
from sqlalchemy import Column, Integer


class Kassas(Base):
    __tablename__ = 'kassas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Integer, nullable=False)
    branch_id = Column(Integer, nullable=False)
