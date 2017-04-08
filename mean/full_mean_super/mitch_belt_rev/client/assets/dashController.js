app.controller('dashController', ['$scope', 'reviewFactory', '$location', function($scope, reviewFactory, $location){
  function currentUser(){
    reviewFactory.currentUser(function(data){
      $scope.user = data;
    })
  }
  currentUser();

  $scope.createTopic = function(newTopic){
    reviewFactory.createTopic(newTopic, getTopics);
    $scope.newTopic = {};
  }

  function getTopics(){
    reviewFactory.getTopics(function(data){
      $scope.topics = data;
    })
  }
  getTopics();
}])
