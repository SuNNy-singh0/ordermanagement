from sqlalchemy.orm import Session
from models.product import Products

class ProductService:
    def __init__(self, db: Session):
        self.db = db
    
    def update_stock(self, productid: int, deduct_quantity: int) -> bool:
        product = self.db.query(Products).filter(Products.id == productid).first()
        
        if product and product.stock_qty >= deduct_quantity:
            product.stock_qty -= deduct_quantity
            self.db.commit()
            return True
        return False
    
    def create_product(self, product_data: dict) -> Products:
        product = Products(**product_data)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def get_all_products(self):
        return self.db.query(Products).all()
