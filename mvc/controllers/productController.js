const ProductModel = require('../moduls/productSchema');
const addProduct = async (req, res) => {
    //adding new product
    try {
        const { productname, category, productdetails, price, rating } = req.body;

        const insertedProduct = await ProductModel.create({
            productname,
            category,
            productdetails,
            price,
            rating
        })

        res.status(200).json({
            message: "Product inserted successfully",
            insertedProduct
        })
    } catch (error) {
        console.log(error.message);
        res.status(404).json({
            message: error.message
        })
    }

};
const updateProduct= async (req, res) => {
    try {
        //details of updating the product
        const { id } = req.params
        const { productdetails, price } = req.body;
        //id : params 
        const updatedProduct = await ProductModel.findByIdAndUpdate(id, { productdetails:productdetails,price:price},{new:true})
        res.status(201).json({
            message: "Product data Updated",
            updatedProduct
        })
    } catch (error) {
        console.log(error.message);
        res.status(404).json({
            message: error.message
        })
    }
};
const filterByPrice = async(req,res)=>{
    try {
       const {price} =req.query;
        
       // const filteredProduct =await ProductModel.find({price:{$gte:price}});
       // const filteredProduct =await ProductModel.find({price:{$lte:price}});
       const filteredProduct =await ProductModel.find({price:{$eq:price}});
       res.status(200).json({
           filteredProduct
       })
    } catch (error) {
       console.log(error.message);
       res.status(404).json({
           message:error.message
       })
    }

};
module.exports={
    addProduct,
    updateProduct,
    filterByPrice
};