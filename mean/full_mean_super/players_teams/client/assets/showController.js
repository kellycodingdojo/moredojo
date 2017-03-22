app.controller('ShowController', ['$scope', '$routeParams', 'PlayersFactory', function($scope, $routeParams, PlayersFactory){
	function show(id){
		PlayersFactory.show(id, function(data){
			$scope.user = data;
		})
	}
	show($routeParams.id);
}])