app.controller('showController', ['$scope', '$routeParams', 'qaFactory', function($scope, $routeParams, qaFactory){
  function showQuestion(id){
    qaFactory.showQuestion(id, function(data){
      $scope.question = data;
    })
  }
  showQuestion($routeParams.id);

  $scope.likeAnswer = function(id, callbackId){
    qaFactory.likeAnswer(id, callbackId, showQuestion);
  }
}])
