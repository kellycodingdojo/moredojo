var serverController = require('./../controller/server_controller.js')
var topic_Controller = require('./../controller/topic_controller.js')
var post_Controller = require('./../controller/post_controller.js')
var comment_Controller = require('./../controller/comment_controller.js')

module.exports = function(app){
	app.post('/register', serverController.register);
	app.post('/login', serverController.login);
	app.get('/logout', serverController.logout);
	app.get('/current', serverController.current);

	app.get('/topics', topic_Controller.getTopics);
	app.post('/topic', topic_Controller.createTopic);
	// app.get('/posts', serverController.getPosts);
	// app.post('/post', serverController.createPost);
	// app.post('/comment/:post_id', serverController.createComment);
}

