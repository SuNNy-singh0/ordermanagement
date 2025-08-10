from sqlalchemy.orm import Session
from sqlalchemy import text
from models.order import Order
from schemas.product import ProductSalesDto, ProductRevenueDTO


class OrderService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_top_selling_products(self):
        query = text("""
            SELECT 
                p.id AS productid, 
                p.name AS name, 
                SUM(o.quantiy) AS totalsold
            FROM 
                orders o
            JOIN 
                products p ON o.productid = p.id
            GROUP BY 
                p.id, p.name
            ORDER BY 
                SUM(o.quantiy) DESC
            OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY
        """)
        
        result = self.db.execute(query)
        rows = result.fetchall()
        
        # Debug: Print column information (remove after debugging)
        if rows:
            print("Available columns:", result.keys())
            print("First row values:", rows[0])
            # Print each column value with its position
            for i, value in enumerate(rows[0]):
                print(f"Column {i}: {value}")
        
        return [ProductSalesDto(
            productid=row[0],      # First column - productid
            name=row[1],           # Second column - name
            totalSold=row[2]       # Third column - totalsold
        ) for row in rows]

    def get_total_revenue_per_product(self):
        query = text("""
            SELECT
                p.id AS productid,
                p.name AS name,
                SUM(o.quantiy * p.price) AS totalrevenue
            FROM
                orders o
            JOIN
                products p ON o.productid = p.id
            GROUP BY
                p.id, p.name
            ORDER BY
                totalrevenue DESC
            OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY
        """)
        
        result = self.db.execute(query)
        rows = result.fetchall()
        
        return [ProductRevenueDTO(
            productid=row[0],        # First column - productid
            name=row[1],             # Second column - name  
            totalRevenue=row[2]      # Third column - totalrevenue
        ) for row in rows]
