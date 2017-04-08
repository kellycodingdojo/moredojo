var mongoose = require('mongoose');
var User = mongoose.model('User');
var Question = mongoose.model('Question');
var Answer = mongoose.model('Answer');


module.exports = {
   current: function(req, res){
    if(req.session.user){
      res.json(req.session.user);
    }
    else{
      res.status(401).send('no user in session');
    }
  },

  register: function(req, res){
    var user = new User(req.body);
    user.save(function(err, data){
      if(err){
        res.status(400).send('user didnt save');
      }
      else{
        req.session.user = data;
        res.sendStatus(200);
      }
    })
  },

  logout: function(req, res){
    req.session.destroy();
    res.redirect('/');
  },





   newQuestion: function(req, res){
   	console.log('******the start of newQuestion server_controll function')
    var question = new Question(req.body);
    question._user = req.session.user;
    console.log("***************")
    question.save(function(err, question){
      if(err){
      	console.log(err)
        res.status(400).send('problem saving question');
      }
      else{
        User.findOne({_id:req.session.user}, function(err, user){

          if(err){
            res.status(400).send(err);
          }
          else{
          console.log("@@@@",question)
          user.questions.push(question);
          user.save(function(err, update_user){
            if(err){
            console.log('this is your error',err)
              res.status(400).send(err);
            }
            else{
              console.log(update_user);
              res.sendStatus(200);
            }
          })
          }
        })
      }
    })
  },

}