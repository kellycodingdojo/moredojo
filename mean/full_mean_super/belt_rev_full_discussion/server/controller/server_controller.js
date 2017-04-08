var mongoose = require('mongoose');
var User = mongoose.model('User');
var Post = mongoose.model('Post');
var Comment = mongoose.model('Comment');
var Topic = mongoose.model('Topic');

module.exports = {
	register: function(req, res){
		var user = new User(req.body);
		console.log(user,'line 10 of servercontroller')
		user.save(function(err,data){
			if(err){
				res.status(400).send("User did not save probably because it already exists")
			}
			else{
				req.session.user = data;
				console.log("Server controller line 13. Printing off session ", req.session.user);
				res.sendStatus(200);
			}
		})
	},
	login: function(req, res){
		User.findOne({email: req.body.email}, function(err, data){
			if(data == null){
				res.status(400).send("User not found.")
			}
			else{
				req.session.user = data;
				res.sendStatus(200);
			}
		})
	},
	current: function(req, res){
		if(req.session.user){
			res.json(req.session.user);
		}else{
			res.status(401).send("No user in session.");
		}
	},
	
	logout: function(req, res){
		req.session.destroy();
		res.redirect('/')
	},
}