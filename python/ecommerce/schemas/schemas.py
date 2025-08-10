from pydantic import BaseModel

class ProductRevenueDTO(BaseModel):
    productid: int  # Long in Java = int in Python
    name: str
    totalRevenue: int

class ProductSalesDto(BaseModel):
    productid: int  # Long in Java = int in Python  
    name: str
    totalSold: int
