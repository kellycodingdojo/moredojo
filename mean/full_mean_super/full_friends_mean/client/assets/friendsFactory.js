app.factory('FriendsFactory', ['$location', '$http', function($location, $http){
	var factory = {};
	factory.getFriends = function(callback){
		$http({
			url:'/friends',  // this is going server side routes. 
			method: 'GET'	// this is what goes first on the servser sides routes.js* such as app.get or app.post, ect.. angular adds put and delete like post and gets
		}).then(function(res){
			callback(res.data); // this call back is refering to the corresponding controller.js function. 
			// <--cont-- we grab the data by id save it into the scope.user and pass it as the call back. 
		})
	}
	factory.newFriend = function(friend){
		$http({
			url:'/friends', 
			method:"POST", 
			data: friend
		}).then(function(res){ // this runs if all goes well. 
			$location.url('/')
		}, function(res){ // fires if something goes wrong
			console.log(res);
		})
	}
	factory.show = function(id, callback){
		$http({
			url:'/friends/' + id,
			method: 'GET'
		}).then(function(res){
			callback(res.data);
		}, function(res){
			console.log(res);
		})

	}
	factory.edit = function(friend, id){
		$http({
			url: '/friends/' + id,
			method: 'PUT', 
			data: friend
		}).then(function(res){
			$location.url('/show/' + id);
		}, function(res){
			console.log(res);
		})
	}
	factory.deleteUser = function(id, callback){
		$http({
			url:'/friends/' + id,
			method: 'DELETE', 
		}).then(function(res){
			callback();
		})
	}
	return factory;
}])