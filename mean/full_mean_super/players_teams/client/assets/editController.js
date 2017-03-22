app.controller('EditController', ['$scope', '$routeParams', 'PlayersFactory', function($scope, $routeParams, PlayersFactory){
	function show(id){
		PlayersFactory.show(id, function(data){
			$scope.player = data;
		})
	}
	show($routeParams.id);
	$scope.editPlayer = function(player, id){
		PlayersFactory.edit(player, id);
	}
}])