app.controller('dashController', ['$scope', 'ice_creamFactory', '$location', function($scope, ice_creamFactory, $location ){
  function currentUser(){
    ice_creamFactory.currentUser(function(data){
      $scope.user = data;
    })
  }
  currentUser();


 
  


}])



