const express =require('express');
const {addProduct,updateProduct,filterByPrice} =require('../controllers/productController')

// creating cusotm route;
const ProductRoute =express.Router();

ProductRoute.post('/add',addProduct);
ProductRoute.post('/update',updateProduct);
ProductRoute.post('/filterPrice',filterByPrice);

module.exports =ProductRoute;