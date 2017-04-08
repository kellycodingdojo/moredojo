app.controller('LoginController', ['$scope', '$location', 'DashFactory', function($scope, $location, DashFactory){
	$scope.register = function(user){
		DashFactory.register(user);
	}
	$scope.login = function(user){
		DashFactory.login(user);
	}
}])

