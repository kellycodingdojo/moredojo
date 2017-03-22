var express = require('express');
// Create an Express App
var app = express();
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');

var mongoose = require('mongoose')

mongoose.connect('mongodb://localhost/mongeese')

var CarSchema = new mongoose.Schema({
 name: {type: String, required:true},
 horsepower: {type: Number, required:true },
 paintColors: []
})

mongoose.model('Car', CarSchema);
var Car = mongoose.model('Car')
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Require path
var path = require('path');
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');

app.get('/', function(req, res){
	Car.find({}, function(err, data){
		if(err){
			console.log(err);
		}
		else{
			res.render('index', {cars: data})	
		}
	})
})

app.get('/car/new', function(req, res){
	res.render('new')
})

app.get('/car/:id', function(req, res){
	Car.findOne({_id: req.params.id}, function(err, data){
		if(err){
			console.log(err);
		}
		else{
			console.log(data);
			res.render('show', {car: data})
			
		}
	})
})


app.get('/car/edit/:id', function(req, res){
	Car.findOne({_id: req.params.id}, function(err, data){
		if(err){
			console.log(err);
		}
		else{
			res.render('edit', {car: data})
			
		}
	})
})

app.post('/car', function(req, res){
	var car = new Car(req.body);
	car.save(function(errors, data){
		if(errors){
			console.log("There were errors")
			console.log(errors);
			res.redirect('/car/new')
		}
		else{
			console.log(data);
			res.redirect(('/car/' + data._id));
		}
	})
})

app.post('/car/:id', function(req, res){
	Car.update({_id: req.params.id}, req.body, function(err,data){
		if(err){
			console.log(err)
		}else{
			res.redirect('/')			
		}
	})
})

app.post('/car/delete/:id', function(req, res){
	Car.remove({_id: req.params.id}, function(err){
		if(err){
			console.log(err);
		}
		res.redirect('/')
	})
})

app.listen(6789);	