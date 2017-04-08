var mongoose = require('mongoose');
var Question = mongoose.model('Question');
var Answer = mongoose.model('Answer');

module.exports = {
  login: function(req, res){
    req.session.user = req.body.name;
    res.sendStatus(200);
  },

  current: function(req, res){
    if(req.session.user){
      res.json(req.session.user);
    }
    else{
      res.status(401).send('no user in session');
    }
  },

  logout: function(req, res){
    req.session.destroy();
    res.redirect('/');
  },

  submitQuestion: function(req, res){
    var question = new Question(req.body);
    question.save(function(err, data){
      if(err){
        res.status(400).send(err);
      }
      else{
        res.sendStatus(200);
      }
    })
  },

  getQuestions: function(req, res){
    Question.find({}, function(err, data){
      if(err){
        res.status(400).send(err);
      }
      else{
        res.json(data);
      }
    })
  },

  findQuestion: function(req, res){
    Question.findOne({_id:req.params.id}, function(err, data){
      if(data == null){
        res.status(400).send(err);
      }
      else{
        res.json(data);
      }
    })
  },

  submitAnswer: function(req, res){
    Question.findOne({_id:req.params.id}, function(err, question){
      if(err){
        res.status(400).send(err);
      }
      else{
        var answer = new Answer(req.body);
        answer.user = req.session.user;
        answer._question = question._id;
        answer.save(function(err, new_answer){
          if(err){
            res.status(400).send(err);
          }
          else{
            question.answers.push(new_answer);
            question.save(function(err, squestion){
              if(err){
                res.status(400).send(err);
              }
              else{
                res.sendStatus(200);
              }
            })
          }
        })
      }
    })
  },

  showQuestion: function(req, res){
    Question.findOne({_id:req.params.id}).populate('answers').exec(function(err, data){
      if(err){
        res.status(400).send(err);
      }
      else{
        res.json(data);
      }
    })
  },

  likeAnswer: function(req, res){
    Answer.findOne({_id:req.params.id}, function(err, answer){
      if(err){
        res.status(400).send(err);
      }
      else{
        answer.likes += 1;
        answer.save(function(err, sanswer){
          if(err){
            res.status(400).send(err);
          }
          else{
            res.sendStatus(200);
          }
        })
      }
    })
  },

}
