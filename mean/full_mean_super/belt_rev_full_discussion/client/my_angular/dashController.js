app.controller('DashController',['$scope', '$location', 'DashFactory', function($scope, $location, DashFactory){
	function currentUser(){
		DashFactory.currentUser(function(data){
			$scope.user = data;
		});
	}
	function getPosts(){
		DashFactory.getPosts(function(data){
			$scope.posts = data;
		})
	}
	getPosts();
	currentUser();
	$scope.addPost = function(post){
		DashFactory.addPost(post, getPosts);
		$scope.newPost = {};
	}
	$scope.addComment = function(comment, post_id){
		DashFactory.addComment(comment, post_id, getPosts);
	}
}])