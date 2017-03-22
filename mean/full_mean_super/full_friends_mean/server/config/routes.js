var friends = require('../controllers/friends.js');

module.exports = function(app){
	app.get('/friends', friends.index); // these are getting called from the friendsFactory.js on the method line. 
	app.get('/friends/:id', friends.show); // then they are sending to the specfic *__*Controller.js in assets. 
	app.post('/friends', friends.create);
	app.put('/friends/:id', friends.update);
	app.delete('/friends/:id', friends.delete);
}