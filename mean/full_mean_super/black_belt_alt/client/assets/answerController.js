app.controller('answerController', ['$scope', '$routeParams', 'qaFactory', function($scope, $routeParams, qaFactory){
  function findQuestion(id){
    qaFactory.findQuestion(id, function(data){
      $scope.question = data;
    })
  }
  findQuestion($routeParams.id);

  $scope.cancelAnswer = function(){
    $scope.newAnswer = {};
  }

  $scope.submitAnswer = function(questionId, answer){
    qaFactory.submitAnswer(questionId, answer);
  }
}])
