var mongoose = require('mongoose');
var Xman = mongoose.model('Xman');

module.exports = {
	route:function(req,res){
		Xman.find({}, function(err, data){
			if(err){
				console.log(err);
			}
			else{
				res.render('index', {heros: data})	
			}
		})
	},

	render: function(req,res){
		res.render('new');
	},

	show: function(req,res){
		Xman.findOne({_id: req.params.id}, function(err, data){
			if(err){
				console.log(err);
			}
			else{
				console.log(data);
				res.render('show', {heros: data})
			
			}	
		})
	},

	edit: function(req,res){
		Xman.findOne({_id: req.params.id}, function(err, data){
			if(err){
				console.log(err);
			}
			else{
				res.render('edit', {heros: data})
				
			}
		})
	},

	newhero: function(req, res){
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
	},
	update: function(req,res){
		Xman.update({_id: req.params.id}, req.body, function(err,data){
			if(err){
				console.log(err)
			}else{
				res.redirect('/')			
			}
		})
	},

	delete: function(req,res){
		Xman.remove({_id: req.params.id}, function(err){
				if(err) { console.log(err) }
				res.redirect('/')
			}	
		)
	}

}