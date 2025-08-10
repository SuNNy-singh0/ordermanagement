package com.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.Repository.ProductRepo;
import com.entity.Products;

@Service
public class ProductService {
@Autowired
private ProductRepo prepo;
public boolean updatestock(int productid, int deduct_quantity) {
    Optional<Products> targetProduct = prepo.findById(productid);
    if (targetProduct.isPresent()) {
        Products product = targetProduct.get();
        if (product.getStock_qty() >= deduct_quantity) {
            product.setStock_qty(product.getStock_qty() - deduct_quantity);
            prepo.save(product); 
            return true;
        }
    }
    return false;
}
}
