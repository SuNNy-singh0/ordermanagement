from sqlalchemy import Column, Integer, String, Sequence
from database import Base

class Products(Base):
    __tablename__ = "products"
    
    id = Column(Integer, Sequence('order_seq'), primary_key=True, index=True)
    name = Column(String(255))
    price = Column(Integer)
    stock_qty = Column(Integer)
