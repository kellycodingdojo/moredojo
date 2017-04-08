var app = angular.module('app', ['ngRoute', 'ngMessages']);

app.config(function($routeProvider){
	$routeProvider
		.when('/', {
			templateUrl: 'partials/login.html',
			controller: 'LoginController'
		})
		.when('/dash', {
			templateUrl: 'partials/dash.html', 
			controller: 'DashController'
		})
		.when('/topic', {
			templateUrl: 'partials/topic.html', 
			controller: 'DashController'
		})
		.otherwise({
			redirectTo: '/'
		})
})