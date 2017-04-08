app.controller('dashController', ['$scope', 'qaFactory', '$location', function($scope, qaFactory, $location){
  function currentUser(){
    qaFactory.currentUser(function(data){
      $scope.user = data;
    })
  }
  currentUser();

  function getQuestions(){
    qaFactory.getQuestions(function(data){
      $scope.questions = data;
    })
  }
  getQuestions();

}])
