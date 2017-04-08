var app = angular.module('app', ['ngRoute', 'ngMessages']);

app.config(function($routeProvider){
  $routeProvider
  .when('/', {
    templateUrl: 'partials/login.html',
    controller: 'loginController'
  })
  .when('/dash', {
    templateUrl: 'partials/dash.html',
    controller: 'dashController'
  })
  .when('/user/:id',{
    templateUrl: 'partials/user.html',
    controller: 'userController'
  })
  .when('/topic/:id',{
    templateUrl: 'partials/topic.html',
    controller: 'topicController'
  })
  .otherwise({
    redirectTo: '/'
  })
})
