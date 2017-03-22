app.controller('TeamController', ['$scope', '$routeParams', 'PlayersFactory', function($scope, $routeParams, PlayersFactory){
	$scope.addTeam = function(team){
		console.log(team)
		PlayersFactory.newTeam(team);
	}
}])