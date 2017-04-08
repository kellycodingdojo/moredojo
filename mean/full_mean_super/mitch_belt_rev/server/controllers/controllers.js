var mongoose = require('mongoose');
var User = mongoose.model('User');
var Topic = mongoose.model('Topic');
var Post = mongoose.model('Post');
var Comment = mongoose.model('Comment');

module.exports = {
  login: function(req, res){
    User.findOne({name: req.body.name}, function(err, data){
      if(err){
        res.status(400).send('user not found');
      }
      else{
        req.session.user = data;
        res.sendStatus(200);
      }
    })
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

  current: function(req, res){
    if(req.session.user){
      res.json(req.session.user);
    }
    else{
      res.status(401).send('no user in session');
    }
  },

  newTopic: function(req, res){
    var topic = new Topic(req.body);
    topic._user = req.session.user._id;
    topic.save(function(err, topic){
      if(err){
        res.status(400).send('problem saving topic');
      }
      else{
        User.findOne({_id:req.session.user._id}, function(err, user){
          if(err){
            res.status(400).send(err);
          }
          else{
          user.topics.push(topic);
          user.save(function(err, update_user){
            if(err){
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

  getTopics: function(req, res){
    Topic.find({}).populate('_user').exec(function(err, data){
      if(err){
        res.status(400).send('cant get topics');
      }
      else{
        res.json(data);
      }
    })
  },

  showUser: function(req, res){
    User.findOne({_id:req.params.id}, function(err, data){
      if(data == null){
          res.status(400).send('no user found');
      }
      else{
        res.json(data);
      }
    })
  },

  showTopic: function(req, res){
    Topic.findOne({_id:req.params.id}).populate('_user').populate({path:'posts', populate:{path:'_user'}}).populate({path:'posts', populate:{path:'comments', populate:{path:'_user'}}}).exec(function(err, data){
      if(data == null){
        res.status(400).send('no topic found');
      }
      else{
        res.json(data);
      }
    })
  },

  newPost: function(req, res){
    Topic.findOne({_id:req.params.id}, function(err, topic){
      if(err){
        res.status(400).send(err);
      }
      else{
        var post = new Post(req.body);
        post._user = req.session.user._id;
        post._topic = topic._id;
        post.save(function(err, new_post){
          if(err){
            console.log(err);
          }
          else{
            topic.posts.push(new_post);
            topic.save(function(err, stopic){
              if(err){
                conosle.log('cant save topic push')
              }
              else{
                User.findOne({_id:req.session.user._id}, function(err, user){
                  console.log(user);
                  if(err){
                    console.log('couldnt find user');
                  }
                  else{
                    user.posts.push(new_post);
                    user.save(function(err, suser){
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
          }
        })
      }
    })
  },

  newComment: function(req, res){
    Post.findOne({_id:req.params.id}, function(err, post){
      if(err){
        res.status(400).send(res);
      }
      else{
        var comment = new Comment(req.body);
        comment._user = req.session.user;
        comment._post = post._id;
        comment.save(function(err, new_comment){
          if(err){
            res.status(400).send(res);
          }
          else{
            post.comments.push(new_comment);
            post.save(function(err, spost){
              if(err){
                res.status(400).send(res);
              }
              else{
                User.findOne({_id:req.session.user._id}, function(err, user){
                  user.comments.push(new_comment);
                  user.save(function(err, suser){
                    if(err){
                      res.status(400).send(res);
                    }
                    else{
                      res.sendStatus(200);
                    }
                  })
                })
              }
            })
          }
        })
      }
    })
  },

  upvote: function(req, res){
    Post.findOne({_id:req.params.id}, function(err, post){
      if(err){
        res.status(400).send(res);
      }
      else{
        post.upvotes += 1;
        post.save(function(err, spost){
          if(err){
            res.status(400).send(res);
          }
          else{
            res.sendStatus(200);
          }
        })
      }
    })
  },

  downvote: function(req, res){
    Post.findOne({_id:req.params.id}, function(err, post){
      if(err){
        res.status(400).send(res);
      }
      else{
        post.downvotes += 1;
        post.save(function(err, spost){
          if(err){
            res.status(400).send(res);
          }
          else{
            res.sendStatus(200);
          }
        })
      }
    })
  },



}
