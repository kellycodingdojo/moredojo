app.factory('TopicFactory', ['$location', '$http', function($location, $http){
	var factory = {};

	factory.addTopic = function(topic, callback){
		console.log('printing data in the factory ', topic)
		$http({
			url:'/topic', 
			method: 'POST', 
			data: topic
		}).then(function(res){
			console.log(res);
			callback();
		}, function(res){
			console.log(res);
		})
	};
	factory.getTopics = function(callback){
		$http({
			url: '/topics', 
			method: 'GET'
		}).then(function(res){
			console.log(res);
			callback(res.data);
		}, function(res){
			console.log(res);
		})
	};
	return factory;
}])