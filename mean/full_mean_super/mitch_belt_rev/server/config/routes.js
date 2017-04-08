var controllers = require('../controllers/controllers.js');

module.exports = function(app){
  app.post('/login', controllers.login);
  app.post('/register', controllers.register);
  app.get('/current', controllers.current);
  app.post('/topic', controllers.newTopic);
  app.get('/topic', controllers.getTopics);
  app.get('/topic/:id', controllers.showTopic);
  app.get('/user/:id', controllers.showUser);
  app.post('/post/:id', controllers.newPost);
  app.post('/comment/:id', controllers.newComment);
  app.get('/logout', controllers.logout);
  app.get('/upvote/:id', controllers.upvote);
  app.get('/downvote/:id', controllers.downvote);
}
