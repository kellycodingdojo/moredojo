app.factory('reviewFactory', ['$location', '$http', function($location, $http){
  var factory = {};

  factory.login = function(user){
    $http({
      url: '/login',
      method: 'POST',
      data: user
    }).then(function(res){
      $location.url('/dash');
    }, function(res){
      console.log('angular failure');
    })
  }

  factory.register = function(user){
    $http({
      url: '/register',
      method: "POST",
      data: user
    }).then(function(res){
      $location.url('/dash');
    }, function(res){
      console.log('register failure');
    })
  }

  factory.currentUser = function(callback){
    $http({
      url: '/current',
      method: "GET"
    }).then(function(res){
      callback(res.data);
    }, function(res){
      $location.url('/')
    })
  }

  factory.createTopic = function(newTopic, callback){
    $http({
      url: '/topic',
      method: 'POST',
      data: newTopic
    }).then(function(res){
      callback();
    }, function(res){
      console.log(res);
    })
  }

  factory.getTopics = function(callback){
    $http({
      url: '/topic',
      method: 'GET',
    }).then(function(res){
      callback(res.data);
    }, function(res){
      console.log(res);
    })
  }

  factory.showUser = function(id, callback){
    $http({
      url: '/user/' + id,
      method: 'GET'
    }).then(function(res){
      callback(res.data);
    }, function(res){
      console.log(res);
    })
  }

  factory.showTopics = function(id, callback){
    $http({
      url: '/topic/' + id,
      method: 'GET'
    }).then(function(res){
      callback(res.data);
    }, function(res){
      console.log(res);
    })
  }

  factory.createPost = function(id, post, callback){
    $http({
      url: '/post/' + id,
      method: 'POST',
      data: post
    }).then(function(res){
      callback(id);
    }, function(res){
      console.log(res);
    })
  }

  factory.createComment = function(callid, id, comment, callback){
    $http({
      url: '/comment/' + id,
      method: 'POST',
      data: comment
    }).then(function(res){
      callback(callid);
    }, function(res){
      console.log(res);
    })
  }

  factory.upvote = function(id, callid, callback){
    $http({
      url: '/upvote/' + id,
      method: 'GET'
    }).then(function(res){
      callback(callid);
    }, function(res){
      console.log(res);
    })
  }

  factory.downvote = function(id, callid, callback){
    $http({
      url: '/downvote/' + id,
      method: 'GET'
    }).then(function(res){
      callback(callid);
    }, function(res){
      console.log(res);
    })
  }

  return factory;
}])
