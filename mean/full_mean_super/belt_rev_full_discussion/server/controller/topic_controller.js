var mongoose = require('mongoose');
var User = mongoose.model('User');
var Post = mongoose.model('Post');
var Comment = mongoose.model('Comment');
var Topic = mongoose.model('Topic');

module.exports = {
	getTopics: function(req,res){
	    Topic.find({}).populate('_user').exec(function(err, data){
	      if(err){
	        res.status(400).send("Something went wrong could not get topics")
	      }
	      else{
	        res.json(data);
	      }
	    })
	  },
// Post.find({}).populate('user').populate({path: 'comments', populate: {path: 'user'}}).exec(function(err, data){

	createTopic: function(req, res){
		var topic = new Topic(req.body);
		topic._user = req.session.user._id;
		topic.save(function(err, data){
			if(err){
				console.log(err)
				console.log(topic)
				res.status(400).send("Problem saving topic");
			}
			else{
				res.sendStatus(200);
			}
		})
	},
}

