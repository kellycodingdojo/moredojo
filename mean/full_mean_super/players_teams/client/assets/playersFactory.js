app.factory('PlayersFactory', ['$location', '$http', function($location, $http){
	var factory = {};
	factory.getPlayers= function(callback){
		$http({
			url:'/players',
			method: 'GET'
		}).then(function(res){
			callback(res.data);
		})
	}
	factory.newPlayer= function(player){
		console.log(player)
		$http({
			url:'/players', 
			method:"POST", 
			data: player
		}).then(function(res){
			$location.url('/')
		}, function(res){
			console.log(res);
		})
	}
	factory.show = function(id, callback){
		$http({
			url:'/players/' + id,
			method: 'GET'
		}).then(function(res){
			callback(res.data);
		}, function(res){
			console.log(res);
		})

	}
	factory.edit = function(player, id){
		$http({
			url: '/players/' + id,
			method: 'PUT', 
			data: player
		}).then(function(res){
			$location.url('/show/' + id);
		}, function(res){
			console.log(res);
		})
	}
	factory.deleteUser = function(id, callback){
		$http({
			url:'/players/' + id,
			method: 'DELETE', 
		}).then(function(res){
			callback();
		})
	}

	factory.getTeam= function(callback){
		$http({
			url:'/teams',
			method: 'GET'
		}).then(function(res){
			callback(res.data);
		})
	}
	factory.newTeam= function(team){
		console.log(team,'this is line 63 on playersfactory')
		$http({
			url:'/teams', 
			method:"POST", 
			data: team
		}).then(function(res){
			$location.url('/')
		}, function(res){
			console.log(res);
		})
	}

	factory.deleteTeam = function(id, callback){
		$http({
			url:'/teams/' + id,
			method: 'DELETE', 
		}).then(function(res){
			callback();
		})
	}

	factory.getAssociations= function(callback){
		$http({
			url:'/association',
			method: 'GET'
		}).then(function(res){
			callback(res.data);
		})
	}

	factory.addAssociation= function(player){
		console.log(player)
		$http({
			url:'/association', 
			method:"POST", 
			data: player
		}).then(function(res){
			$location.url('/association')
		}, function(res){
			console.log(res);
		})
	}



	return factory;
}])