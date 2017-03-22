var express = require('express');
// Create an Express App
var app = express();
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');

var mongoose = require('mongoose')

mongoose.connect('mongodb://localhost/mongeese')

var XmanSchema = new mongoose.Schema({
 name: {type: String, required:true},
 age: {type: Number, required:true },
 power: {type: String, required:true },
 HeroColors: []
})

mongoose.model('Xman', XmanSchema);
var Xman = mongoose.model('Xman')
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
	Xman.find({}, function(err, data){
		if(err){
			console.log(err);
		}
		else{
			res.render('index', {heros: data})	
		}
	})
})

app.get('/hero/new', function(req, res){
	res.render('new')
})

app.get('/hero/:id', function(req, res){
	Xman.findOne({_id: req.params.id}, function(err, data){
		if(err){
			console.log(err);
		}
		else{
			console.log(data);
			res.render('show', {heros: data})
			
		}
	})
})

app.get('/hero/edit/:id', function(req, res){
	Xman.findOne({_id: req.params.id}, function(err, data){
		if(err){
			console.log(err);
		}
		else{
			res.render('edit', {heros: data})
			
		}
	})
})

app.post('/hero', function(req, res){
	var hero = new Xman(req.body);
	hero.save(function(errors, data){
		if(errors){
			console.log("There were errors")
			console.log(errors);
			res.redirect('/hero/new')
		}
		else{
			console.log(data);
			res.redirect(('/hero/' + data._id));
		}
	})
})

app.post('/hero/:id', function(req, res){
	Xman.update({_id: req.params.id}, req.body, function(err,data){
		if(err){
			console.log(err)
		}else{
			res.redirect('/')			
		}
	})
})

app.post('/hero/delete/:id', function(req, res){
	Xman.remove({_id: req.params.id}, function(err){
		if(err){
			console.log(err);
		}
		res.redirect('/')
	})
})

app.listen(6789);