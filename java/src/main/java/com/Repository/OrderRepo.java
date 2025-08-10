package com.Repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.dto.ProductRevenueDTO;
import com.dto.ProductSalesDto;
import com.entity.Order;
import com.entity.Products;

public interface OrderRepo extends JpaRepository<Order, Integer>{
	@Query(value = """
		    SELECT 
		        p.id AS "productid", 
		        p.name AS "name", 
		        SUM(o.quantiy) AS "totalSold"
		    FROM 
		        orders o
		    JOIN 
		        products p ON o.productid = p.id
		    GROUP BY 
		        p.id, p.name
		    ORDER BY 
		        SUM(o.quantiy) DESC
		    OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY
		    """, nativeQuery = true)
		List<ProductSalesDto> findTopSellingProducts();
	
	@Query(value = """
		   SELECT
    p.id AS productid,
    p.name AS name,
    SUM(o.quantiY * p.price) AS totalRevenue
FROM
    orders o
JOIN
    products p ON o.productid = p.id
GROUP BY
    p.id, p.name
ORDER BY
    totalRevenue DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY
		    """, nativeQuery = true)
	    List<ProductRevenueDTO> getTotalRevenuePerProduct();


}
