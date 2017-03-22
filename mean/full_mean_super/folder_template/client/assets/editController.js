app.controller('EditController', ['$scope', '$routeParams', 'FriendsFactory', function($scope, $routeParams, FriendsFactory){
	function show(id){
		FriendsFactory.show(id, function(data){
			$scope.friend = data;
		})
	}
	show($routeParams.id);
	$scope.editFriend = function(friend, id){
		FriendsFactory.edit(friend, id);
	}
}])