app.controller('questionController', ['$scope', '$routeParams', 'ice_creamFactory', function($scope, $routeParams, ice_creamFactory){
	
	$scope.createQuestion = function(id, post){
	    ice_creamFactory.createQuestion(id, post);
	    $scope.newQuestion = {};
  }
}])