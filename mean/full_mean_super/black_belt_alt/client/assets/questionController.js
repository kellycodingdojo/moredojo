app.controller('questionController', ['$scope', 'qaFactory', function($scope, qaFactory){
  $scope.cancelQuestion = function(){
    $scope.newQuestion = {};
  }

  $scope.submitQuestion = function(question){
    qaFactory.submitQuestion(question);
  }
}])
