app.controller('userController', ['$scope', 'ice_creamFactory', '$location', function($scope, ice_creamFactory, $location){

  // $scope.login = function(user){
  //   ice_creamFactory.login(user);
  //   $scope.user = {};
  // }
 $scope.register = function(user){
    ice_creamFactory.register(user);
    $scope.reguser = {};
  }


}])