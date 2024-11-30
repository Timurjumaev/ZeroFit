from sqlalchemy.orm import relationship, backref
from db import Base
from sqlalchemy import Column, Integer, String, DateTime, func, text
from models.sales import Sales


class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(255), nullable=False)
    sale_id = Column(Integer, nullable=True)
    money = Column(Integer, nullable=False)
    comment = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now() + text("INTERVAL 5 HOUR"))
    branch_id = Column(Integer, nullable=False)

    sale = relationship('Sales', foreign_keys=[sale_id],
                        primaryjoin=lambda: Sales.id == Transactions.sale_id,
                        backref=backref("transactions"))
