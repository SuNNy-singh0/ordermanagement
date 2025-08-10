from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.product import ProductCreate, ProductResponse
from services.product_service import ProductService
from typing import List

router = APIRouter()

@router.post("/create-product", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        service = ProductService(db)
        created_product = service.create_product(product.dict())
        return {"message": "Product created successfully!"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error in Creating Product"
        )

@router.get("/all-products", response_model=List[ProductResponse])
async def get_all_products(db: Session = Depends(get_db)):
    try:
        service = ProductService(db)
        products = service.get_all_products()
        return products
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving products"
        )
