var controller = require('../controllers/controller.js');

module.exports = function(app){
  app.post('/login', controller.login);
  app.get('/logout', controller.logout);
  app.get('/current', controller.current);
  app.post('/submitQuestion', controller.submitQuestion);
  app.get('/getQuestions', controller.getQuestions);
  app.get('/findQuestion/:id', controller.findQuestion);
  app.post('/submitAnswer/:id', controller.submitAnswer);
  app.get('/showQuestion/:id', controller.showQuestion);
  app.get('/likeAnswer/:id', controller.likeAnswer);
}
