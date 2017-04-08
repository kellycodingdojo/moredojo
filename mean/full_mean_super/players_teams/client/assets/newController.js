app.controller('NewController', ['$scope', '$routeParams', 'PlayersFactory', function($scope, $routeParams, PlayersFactory){
	$scope.addPlayer = function(player){
		console.log(player)
		PlayersFactory.newPlayer(player);
		$scope.newPlayer = {}
	}
}])