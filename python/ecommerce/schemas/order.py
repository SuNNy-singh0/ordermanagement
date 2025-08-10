from pydantic import BaseModel
from datetime import date
from typing import Optional

class OrderCreate(BaseModel):
    productid: int
    quantiy: int  # Keeping the typo to match your original

class OrderResponse(BaseModel):
    orderid: int
    productid: int
    quantiy: int
    totalprice: int
    order_date: date
    
    class Config:
        from_attributes = True
