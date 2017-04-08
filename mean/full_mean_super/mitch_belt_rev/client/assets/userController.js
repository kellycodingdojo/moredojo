app.controller('userController', ['$scope', '$routeParams', 'reviewFactory', function($scope, $routeParams, reviewFactory){
  function showUser(id){
    reviewFactory.showUser(id, function(data){
      $scope.user = data;
    })
  }
  showUser($routeParams.id);
}])
