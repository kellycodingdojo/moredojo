app.controller('HomeController', ['$scope', '$routeParams', 'FriendsFactory', function($scope, $routeParams, FriendsFactory){
	function getUsers(){
		FriendsFactory.getFriends(function(data){
			$scope.friends = data;
		})
	}
	getUsers();
	$scope.deleteUser = function(id){
		FriendsFactory.deleteUser(id, getUsers); // the get users is the call abck that you are passing the deleteUser function in factory. 
	}
}])