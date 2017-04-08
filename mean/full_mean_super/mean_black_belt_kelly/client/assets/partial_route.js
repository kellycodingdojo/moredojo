var app = angular.module('app', ['ngRoute', 'ngMessages']);

app.config(function($routeProvider){
  $routeProvider
  .when('/', {
    templateUrl: 'partials/login.html',
    controller: 'userController'
  })
  .when('/dash', {
    templateUrl: 'partials/dash.html',
    controller: 'dashController'
  })
  .when('/new_question',{
    templateUrl: 'partials/new_question.html',
    controller: 'questionController'
  })
  .when('/home' ,{
    templateUrl: 'partials/dash.html',
    controller: 'dashController'
  })
  // .when('/user/:id',{
  //   templateUrl: 'partials/user.html',
  //   controller: 'userController'
  // })
  
  .otherwise({
    redirectTo: '/'
  })
})