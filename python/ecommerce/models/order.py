from sqlalchemy import Column, Integer, Date, Sequence
from database import Base
from datetime import date

class Order(Base):
    __tablename__ = "orders"
    
    orderid = Column(Integer, Sequence('order_seq'), primary_key=True, index=True)
    productid = Column(Integer)
    quantiy = Column(Integer)  # Keeping the typo to match your original
    totalprice = Column(Integer)
    order_date = Column(Date, default=date.today)
