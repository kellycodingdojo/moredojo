app.controller('loginController', ['$scope', 'qaFactory', '$location', function($scope, qaFactory, $location){
  $scope.login = function(user){
    qaFactory.login(user);
    $scope.user = {};
  }
}])
