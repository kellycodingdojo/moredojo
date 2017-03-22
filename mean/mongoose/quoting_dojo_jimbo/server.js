// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');
// Require path
var path = require('path');
//require mongoose
var mongoose = require('mongoose');
// This is how we connect to the mongodb database using mongoose -- "basic_mongoose" is the name of
//   our db in mongodb -- this should match the name of the db you are going to use for your project.
mongoose.connect('mongodb://localhost/basic_mongoose');
// Use native promises to avoid breaking in future due to deprecation
mongoose.Promise = global.Promise;

var UserSchema = new mongoose.Schema({
	author: {type:String, required:true, minlength: 2},
	quote: {type:String, required:true, maxlength: 50}
}, {timestamps: true });
// var PostSchema = new mongoose.Schema({
// 	post: {type:String, maxlength:255}
// }) for display purposes another collection
mongoose.model('User', UserSchema); // We are setting this Schema in our Models as 'User'
// mongoose.model('Post', PostSchema);
var User = mongoose.model('User'); // We are retrieving this Schema from our Models, named 'User'
// var Post = mongoose.model('Post');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// app.use(express.static(__dirname + './static'))
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
// Routes
// Root Request
app.get('/', function(req, res) {
    	res.render('index');
})
    // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
// Add User Request 
app.post('/quotes', function(req, res){//forms usually post requests
    console.log("Body is ", req.body);
    var user = new User(req.body);
    user.save(function(errors, data){
    	if(errors){
    		console.log(errors);
    	}
    	console.log("Data is ", data);
    	res.redirect('/quotes');
    })
    // This is where we would add the user from req.body to the database.
})
app.get('/quotes', function(req, res){//a tags always get requests
    User.find().sort({ createdAt: -1 }).exec(function(errors, data){
        console.log("THIS IS WHAT WE HAVE:\n\n\n", data)
        if(errors){
            console.log(errors);
        }
        res.render('quotes', {users: data});
    })
})
// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
