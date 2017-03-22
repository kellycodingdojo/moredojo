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
io.sockets.on('connection', function(socket){

	socket.emit('load_messages', {messages: messages});
	
	socket.on('new_user', function(data){
		io.emit('user_added', {name: data.name})
	});

	socket.on('send_message', function(data){
		messages.push(data.name + ": " + data.message);
		io.emit('new_message', {name: data.name, message: data.message});
	})
})