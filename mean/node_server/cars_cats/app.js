var fs = require('fs'),
    http = require('http'),
    port = 7077;

var server = http.createServer(function server(req, response){
  // Figure out which file the HTTP request is looking for
   if(req.url === '/styles'){
    fs.readFile('./stylesheet/styles.css', 'utf8', function(errors, contents){
     response.writeHead(200, {'Content-type': 'text/css'});
     response.write(contents);
     response.end();
    })
  }

    else if(req.url === '/') {
      fs.readFile('views/cars.html', 'utf8', function (errors, contents){
          response.writeHead(200, {'Content-Type': 'text/html'});
          response.write(contents); 
          response.end();
    });
  }

     else if(req.url === '/cats') {
        fs.readFile('views/cats.html', 'utf8', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(contents); 
            response.end();
      });
    }
    
    else if(req.url === '/car1'){
     fs.readFile('./images/car1.jpg', function(errors, contents){
      response.writeHead(200, {'Content-type': 'image/jpg'});
      response.write(contents);
      response.end();
    }); 
  }
 
    else if(req.url === '/car2'){
     fs.readFile('./images/car2.jpg', function(errors, contents){
      response.writeHead(200, {'Content-type': 'image/jpg'});
      response.write(contents);
      response.end();
    }); 
  }

   

    else if(req.url === '/cat1'){
     fs.readFile('./images/cats1.jpg', function(errors, contents){
      response.writeHead(200, {'Content-type': 'image/jpg'});
      response.write(contents);
      response.end();
    }); 
  }

  else if(req.url === '/cat2'){
     fs.readFile('./images/cat2.jpg', function(errors, contents){
      response.writeHead(200, {'Content-type': 'image/jpg'});
      response.write(contents);
      response.end();
    }); 
  }


  else { // If file is null, not found
    response.writeHead(404);
    response.end("File not found!");
  }
});

server.listen(port, function(){
  console.log("Running on port: ", port);
});