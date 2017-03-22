app.controller('ShowController', ['$scope', '$routeParams', 'FriendsFactory', function($scope, $routeParams, FriendsFactory){
	function show(id){
		FriendsFactory.show(id, function(data){
			$scope.user = data;
		})
	}
	show($routeParams.id);
}])