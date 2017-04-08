app.factory('ice_creamFactory', ['$location', '$http', function($location, $http){
  var factory = {};

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
  },

  factory.currentUser = function(callback){
    $http({
      url: '/current',
      method: "GET"
    }).then(function(res){
      callback(res.data);
    }, function(res){
      $location.url('/')
    })
  },

  factory.createQuestion = function(question, callback){
    console.log(question)
    $http({
      url: '/question',
      method: 'POST',
      data: question
    // }).then(function(res){
    //   callback();
    // }, function(res){
    //   console.log(res);
     })
  }



  return factory;
}])

