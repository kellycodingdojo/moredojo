app.controller('loginController', ['$scope', 'reviewFactory', '$location', function($scope, reviewFactory, $location){

  $scope.login = function(user){
    reviewFactory.login(user);
    $scope.user = {};
  }

  $scope.register = function(user){
    reviewFactory.register(user);
    $scope.reguser = {};
  }
}])
