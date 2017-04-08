app.controller('DashController',['$scope', '$location', 'DashFactory','TopicFactory', function($scope, $location, DashFactory, TopicFactory){
	function currentUser(){
		DashFactory.currentUser(function(data){
			$scope.user = data;
		});
	}
	function getTopics(){
		TopicFactory.getTopics(function(data){
			$scope.topics = data;
		})
	}
	// getPosts();
	currentUser();
	getTopics();


	$scope.addTopic= function(topic){
		TopicFactory.addTopic(topic, getTopics);
		$scope.newTopic= {};
	}


	

	// function getPosts(){
	// 	DashFactory.getPosts(function(data){
	// 		$scope.posts = data;
	// 	})
	// }
	// getPosts();
	// currentUser();
	// $scope.addPost = function(post){
	// 	DashFactory.addPost(post, getPosts);
	// 	$scope.newPost = {};
	// }
	// $scope.addComment = function(comment, post_id){
	// 	DashFactory.addComment(comment, post_id, getPosts);
	// }
}])