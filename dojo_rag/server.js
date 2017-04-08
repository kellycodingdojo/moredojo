var express = require('express');

var app = express();

app.use(express.static(__dirname + '/static'));

app.set('views', __dirname + '/views');

app.set('view engine', 'ejs');

app.get('/', function(req, res){
	res.render('index');
})

var server = app.listen(6789);
var io = require('socket.io').listen(server);

var messages = [];
var user_names = [];
var connections = [];

io.sockets.on('connection', function(socket){
	connections.push(socket)
	console.log('connected: %s sockets')

	socket.emit('load_messages', {messages: messages});
	
	function update_list(){
		io.emit('user_names', {name: user_names});
	}
	update_list()
	

	socket.on('new_user', function(data){
		io.emit('user_added', {name: data.name})
		user_names.push({name: data.name, id:socket.id});

	});

	socket.on('send_message', function(data){
		console.log(data, 'line 34')
		messages.push(data.name + ": " + data.message);
		io.emit('new_message', {name: data.name, message: data.message});
		

	});
	socket.on('disconnect', function() {
      console.log('Got disconnect!',socket.id);
      for(var i = 0; i < user_names.length; i++){
      	if(user_names[i].id == socket.id){
      		console.log(user_names[i].id, 'line 51');
      		socket.broadcast.emit('user_disconnected',{name:user_names[i].name} )
      		user_names.splice(i,1);
      		update_list()

      		break;
      	}
      }
  })

  
})
 
