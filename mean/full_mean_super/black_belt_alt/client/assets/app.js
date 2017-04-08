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
  .when('/new_question', {
    templateUrl: 'partials/new_question.html',
    controller: 'questionController'
  })
  .when('/question/:id/new_answer', {
    templateUrl: 'partials/new_answer.html',
    controller: 'answerController'
  })
  .when('/question/:id', {
    templateUrl: 'partials/show.html',
    controller: 'showController'
  })
  .otherwise({
    redirectTo: '/'
  })
})
