var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var session = require('express-session');
var app = express();

var sessionConfig = {
  secret: "secret",
  resave: false,
  saveUninitialized: true,
  name: 'mySession',
  cookie: {
    secure: false,
    httpOnly: false,
    maxAge: 9001000000000
  }
}

app.use(session(sessionConfig));
app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'client')));
app.use(express.static(path.join(__dirname, 'bower_components')));

require('./server/config/mongoose.js');
require('./server/config/routes.js')(app);

app.listen(8000, function(){})
