app.controller('AssociationController', ['$scope', '$routeParams', 'PlayersFactory', function($scope, $routeParams, PlayersFactory){
	function getTeam(){
		PlayersFactory.getTeam(function(data){
			$scope.teams = data;
		})
	}
	function getPlayers(){
		PlayersFactory.getPlayers(function(data){
			$scope.players = data;
		})
	}
	
	function getAssociations(){
		PlayersFactory.getAssociations(function(data){
			$scope.associations = data;
		})
	}

	
	getTeam();
	getPlayers();
	getAssociations();
	$scope.addAssociation = function(){
		PlayersFactory.addAssociation($scope.newA, getAssociations);
		console.log($scope.newA)
		$scope.newA = {};
	}

}])