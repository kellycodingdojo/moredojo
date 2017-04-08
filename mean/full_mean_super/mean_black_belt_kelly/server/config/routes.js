var controllers = require('../controller/server_controller.js');

module.exports = function(app){
  app.post('/register', controllers.register);
  app.get('/current', controllers.current);
  app.get('/logout', controllers.logout);
  app.post('/question', controllers.newQuestion);
  // app.get('/topic', controllers.getTopics);
  // app.get('/topic/:id', controllers.showTopic);
  // app.get('/user/:id', controllers.showUser);
  // app.post('/post/:id', controllers.newPost);
  // app.post('/comment/:id', controllers.newComment);
  // app.get('/upvote/:id', controllers.upvote);
  // app.get('/downvote/:id', controllers.downvote);
  // app.get('/home', controllers.home);
}