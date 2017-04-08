app.factory('PlayerFactory', function)(){
	var factory = {}
factory.getPlayers = function(callback){
	callback(players)
}

// factory.addPlayers = function(player){
// 	players.push(player);
// };

factory.getTeams = function(callback){
	callback(teams);
}

// factory.addTeam = function(team){
// 	teams.push(team)
// }

factory.getAssociations = function(callback){
	callback(associations);
}

// factory.addAssociation = function(association){
// 	associations.push(association);
// }
}

return factory;

})