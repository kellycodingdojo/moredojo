var players = require('../controllers/players.js');


module.exports = function(app){
	app.get('/players', players.index);
	app.get('/players/:id', players.show);
	app.post('/players', players.create);
	app.put('/players/:id', players.update);
	app.delete('/players/:id', players.delete);
	app.get('/teams', players.team_index);
	app.post('/teams', players.team_create);
	app.delete('/teams/:id', players.team_delete);
	app.post('/association', players.association_index);
	app.get('/association', players.get_associations);
}