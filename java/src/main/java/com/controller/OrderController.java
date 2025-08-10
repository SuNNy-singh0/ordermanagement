package com.controller;

import java.time.LocalDate;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.Repository.OrderRepo;
import com.Repository.ProductRepo;
import com.dto.ProductRevenueDTO;
import com.dto.ProductSalesDto;
import com.entity.Order;
import com.entity.Products;
import com.service.OrderService;
import com.service.ProductService;

@RestController
@CrossOrigin(origins = {"http://localhost:5173"}, allowCredentials = "true")
public class OrderController {
@Autowired
private OrderRepo orepo;
@Autowired
private ProductRepo prepo;
@Autowired
private OrderService orderservice;
@Autowired
private ProductService productservice;

@PostMapping("/make-order")
public ResponseEntity<?> createproduct(@RequestBody Order order){
	try {
	Order temporder  = new Order();
	Optional<Products> checkproduct  = prepo.findById(order.getProductid());
	if(order.getQuantiy()<= checkproduct.get().getStock_qty()) {
		temporder.setProductid(order.getProductid());
		temporder.setQuantiy(order.getQuantiy());
		temporder.setTotalprice(checkproduct.get().getPrice()*order.getQuantiy());
		temporder.setOrder_date(LocalDate.now());
		orepo.save(temporder);
		productservice.updatestock(order.getProductid(), order.getQuantiy());
		 return ResponseEntity.status(HttpStatus.CREATED).body("order placed Sucessfully");
	}
	else {
		return ResponseEntity.status(HttpStatus.NOT_ACCEPTABLE).body("InSufficient order");
	}
	 
	}
	catch(Exception e) {
		return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error in Creating Product");
	}

}
@GetMapping("/topproduct")
public ResponseEntity<List<ProductSalesDto>> getTopProduct() {
    return ResponseEntity.ok(orderservice.getTopProducts());
}

@GetMapping("/revenue-per-product")
public ResponseEntity<List<ProductRevenueDTO>> getRevenuePerProduct() {
    List<ProductRevenueDTO> revenueList = orderservice.getRevenuePerProduct();
    return ResponseEntity.ok(revenueList);
}
}
