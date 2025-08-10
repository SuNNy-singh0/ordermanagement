package com.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.entity.Products;

public interface ProductRepo extends JpaRepository<Products, Integer> {

}
