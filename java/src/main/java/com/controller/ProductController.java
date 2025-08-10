package com.controller;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.Repository.ProductRepo;
import com.entity.Products;

@RestController
@CrossOrigin(origins = {"http://localhost:5173"}, allowCredentials = "true")
public class ProductController {
    @Autowired
	private ProductRepo repo;
    
    @PostMapping("/create-product")
    public ResponseEntity<?> createproduct(@RequestBody Products product){
    	try {
    	Products temp  = new Products();
    	temp.setName(product.getName());
    	temp.setPrice(product.getPrice());
    	temp.setStock_qty(product.getStock_qty());
    	repo.save(temp);
    	 return ResponseEntity.status(HttpStatus.CREATED).body("Product created successfully!");
    	}
    	catch(Exception e) {
    		return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error in Creating Product");
    	}
    }
    @GetMapping("/all-products")
    public ResponseEntity<List<Products>> getAllProducts() {
        try {
            List<Products> products = repo.findAll();
            return ResponseEntity.ok(products);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }
   
}
