var app = angular.module('app', ['ngRoute', 'ngMessages']);

app.config(function($routeProvider){
	$routeProvider
		.when('/', {
			templateUrl: 'partials/login.html',
			controller: 'LoginController'
		})
		.when('/wall', {
			templateUrl: 'partials/wall.html', 
			controller: 'WallController'
		})
		.otherwise({
			redirectTo: '/'
		})
})