package com.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;

import com.Repository.OrderRepo;
import com.dto.ProductRevenueDTO;
import com.dto.ProductSalesDto;
import com.entity.Products;

@Service
public class OrderService {
	@Autowired
    private OrderRepo orderrepo;
	 public List<ProductSalesDto> getTopProducts() {
	        return orderrepo.findTopSellingProducts();
	    }
	 public List<ProductRevenueDTO> getRevenuePerProduct() {
	        return orderrepo.getTotalRevenuePerProduct();
	    }
}
