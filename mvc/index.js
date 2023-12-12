const express = require('express');
const mongoose =require('mongoose');

const app =express();
const Port =5000;

app.use(express.json());
const connectDb =async()=>{
    try {
        await mongoose.connect('mongodb+srv://raman31293:qwertyuiop@raman.32vvs85.mongodb.net/Flipkart')
        console.log("Connected to database");
    } catch (error) {
        console.log(error.message);
    }
}

connectDb();


// Problem statement for E-commerce(Flipkart);
// Product , Userdetail, Orders, wishlists.
// importing user APIs here
const UserRoute = require('./routes/user.routes')
app.use('/user',UserRoute);
const ProductRoute = require('./routes/product.routes')
app.use('/product',ProductRoute);


app.listen(Port,()=>{
    console.log(`server is working on Port ${Port}`)
})