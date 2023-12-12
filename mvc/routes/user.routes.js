const express =require('express');
const {userRegister,userLogin,updateUserByID} =require('../controllers/userController')

// creating cusotm route;
const UserRoute =express.Router();

UserRoute.post('/register',userRegister);
UserRoute.post('/login',userLogin);
UserRoute.post('/update',updateUserByID);

module.exports =UserRoute;
