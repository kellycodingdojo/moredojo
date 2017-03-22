app.controller('HomeController', ['$scope', '$routeParams', 'PlayersFactory', function($scope, $routeParams, PlayersFactory){
	function getUsers(){
		PlayersFactory.getPlayers(function(data){
			$scope.players = data;
		})
	}
	getUsers();
	$scope.deleteUser = function(id){
		PlayersFactory.deleteUser(id, getUsers);
	}

	function getTeams(){
		PlayersFactory.getTeam(function(data){
			$scope.teams = data;
		})
	}
	getTeams();

	$scope.deleteTeam = function(id){
		PlayersFactory.deleteTeam(id, getTeams);
	}

}])