const express =require('express');
const {commentCreate,getAllComments} =require('../controllers/commentController')

// creating cusotm route;
const CommentRoute =express.Router();

CommentRoute.post('/create',commentCreate);
CommentRoute.post('/getAll',getAllComments);

module.exports =CommentRoute;