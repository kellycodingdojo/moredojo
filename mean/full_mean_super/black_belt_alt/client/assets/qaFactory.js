app.factory('qaFactory', ['$location', '$http', function($location, $http){
  var factory = {};

  factory.login = function(user){
    $http({
      url: '/login',
      method: 'POST',
      data: user
    }).then(function(res){
      $location.url('/dash');
    }, function(res){
      console.log(res);
    })
  }

  factory.currentUser = function(callback){
    $http({
      url: '/current',
      method: "GET"
    }).then(function(res){
      callback(res.data);
    }, function(res){
      $location.url('/');
    })
  }

  factory.submitQuestion = function(question){
    $http({
      url: '/submitQuestion',
      method: 'POST',
      data: question
    }).then(function(res){
      $location.url('/dash');
    }, function(res){
      console.log(res);
    })
  }

  factory.getQuestions = function(callback){
    $http({
      url: '/getQuestions',
      method: 'GET'
    }).then(function(res){
      callback(res.data);
    }, function(res){
      console.log(res);
    })
  }

  factory.findQuestion = function(id, callback){
    $http({
      url: '/findQuestion/' + id,
      method: 'GET'
    }).then(function(res){
      callback(res.data);
    }, function(res){
      console.log(res);
    })
  }

  factory.submitAnswer = function(questionId, answer){
    $http({
      url: '/submitAnswer/' + questionId,
      method: 'POST',
      data: answer
    }).then(function(res){
      $location.url('/dash');
    }, function(res){
      console.log(res);
    })
  }

  factory.showQuestion = function(id, callback){
    $http({
      url: '/showQuestion/' + id,
      method: 'GET'
    }).then(function(res){
      callback(res.data);
    }, function(res){
      console.log(res);
    })
  }

  factory.likeAnswer = function(id, callbackId, callback){
    $http({
      url: '/likeAnswer/' + id,
      method: 'GET'
    }).then(function(res){
      callback(callbackId);
    }, function(res){
      console.log(res);
    })
  }

  return factory;
}])
