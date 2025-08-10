from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    price: int
    stock_qty: int

class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    stock_qty: int
    
    class Config:
        from_attributes = True

class ProductSalesDto(BaseModel):
    productid: int
    name: str
    totalSold: int

class ProductRevenueDTO(BaseModel):
    productid: int
    name: str
    totalRevenue: int
