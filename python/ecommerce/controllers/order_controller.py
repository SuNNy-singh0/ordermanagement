from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.order import OrderCreate, OrderResponse
from schemas.product import ProductSalesDto, ProductRevenueDTO
from services.order_service import OrderService
from services.product_service import ProductService
from models.order import Order
from models.product import Products
from datetime import date
from typing import List

router = APIRouter()

@router.post("/make-order", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        # Check if product exists and has sufficient stock
        product = db.query(Products).filter(Products.id == order.productid).first()
        
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        
        if order.quantiy <= product.stock_qty:
            # Create order
            new_order = Order(
                productid=order.productid,
                quantiy=order.quantiy,
                totalprice=product.price * order.quantiy,
                order_date=date.today()
            )
            
            db.add(new_order)
            db.commit()
            
            # Update stock
            product_service = ProductService(db)
            product_service.update_stock(order.productid, order.quantiy)
            
            return {"message": "order placed Successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Insufficient stock"
            )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error in Creating Order"
        )

@router.get("/topproduct", response_model=List[ProductSalesDto])
async def get_top_products(db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.get_top_selling_products()

@router.get("/revenue-per-product", response_model=List[ProductRevenueDTO])
async def get_revenue_per_product(db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.get_total_revenue_per_product()
