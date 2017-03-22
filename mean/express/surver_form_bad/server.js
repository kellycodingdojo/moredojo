
//load the express module
//load the path module
//load the body-parser
var express = require("express");
var path = require("path");
var bodyParser = require('body-parser');
// invoke var express and store the resulting application in var app
var app = express();
app.use(bodyParser.urlencoded());
app.use(express.static(path.join(__dirname, "./static")));
// setting up ejs and our views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

//we're going to have /routes/index.js handle all of our routing
	app.get('/', function(req, res) {
	 res.render("index");
	})
	// post route for adding a data from a survey
	app.post('/result', function(req, res) {
		submitted_info = {
			name: req.body.name,
			dojo_location: req.body.dojo_location,
			favorite_language: req.body.favorite_language,
			comment: req.body.comment
		};
	 	res.render("result",{user_data: submitted_info});
	})
// setting server to run on port 3000
app.listen(3000, function() {
 console.log("listening on port 3000!");
})