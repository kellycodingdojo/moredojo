app.controller('topicController', ['$scope', '$routeParams', 'reviewFactory', function($scope, $routeParams, reviewFactory){
  function showTopics(id){
    reviewFactory.showTopics(id, function(data){
      $scope.topic = data;
    })
  }
  showTopics($routeParams.id);


  $scope.createPost = function(id, post){
    reviewFactory.createPost(id, post, showTopics);
    $scope.newPost = {};
  }

  $scope.createComment = function(callid, id, comment){
    reviewFactory.createComment(callid, id, comment, showTopics);
    $scope.newComment = {};
  }

  $scope.upvote = function(id, callid){
    reviewFactory.upvote(id, callid, showTopics);
  }

  $scope.downvote = function(id, callid){
    reviewFactory.downvote(id, callid, showTopics);
  }
}])
