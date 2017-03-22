var express = require("express");
var app = express();

app.get('/', function(request, response) {
  response.send("<h1 style='style'>Hello Express</h1>");
})




app.use(express.static(__dirname + "/static")); // this will retreive all the files in the static folder. includeing the css and html ect. 


app.set('views', __dirname + '/views'); 
app.set('view engine', 'ejs'); // ejs is a templating language, we are setting engine views ot it. 



app.listen(8000, function() {
  console.log("listening on port 8000");
})

app.get("/users", function (request, response){
    // hard-coded user data
    var users_array = [
        {name: "Michael", email: "michael@codingdojo.com"}, 
        {name: "Jay", email: "jay@codingdojo.com"}, 
        {name: "Brendan", email: "brendan@codingdojo.com"}, 
        {name: "Andrew", email: "andrew@codingdojo.com"}
    ];
    response.render('users', {users: users_array});
})