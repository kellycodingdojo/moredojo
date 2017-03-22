var mongoose = require('mongoose');
var Player = mongoose.model('Player')
var Team = mongoose.model('Team')
module.exports = {
  index: function(req,res){
    Player.find({}, function(err, data){
      if(err){
        res.status(400).send("Something went wrong.")
      }
      else{
        res.json(data);
      }
    })
  },

  team_index: function(req,res){
      Team.find({}, function(err, data){
        if(err){
          res.status(400).send("Something went wrong.")
        }
        else{
          res.json(data);
        }
      })
    },



  team_create: function(req,res){
    var team = new Team(req.body);
    team.save(function(err,data){
      console.log(team)
      if(err){
        console.log(err)
        res.status(400).send("team was not saved into the database.")
      } 
      else{
      res.sendStatus(200);
    }
    })
  },

  team_delete: function(req,res){
    Team.findOne({_id:req.params.id}, function(err, data){
      if(data == null){
        res.status(400).send("No team found");
      }
      else{
      data.remove();
      res.status(200).send("team was deleted.");
    }
    })
  },
 

  create: function(req,res){
    var player = new Player(req.body);
    player.save(function(err,data){
      if(err){
        console.log(err)
        res.status(400).send("Player was not saved into the database.")
      } 
      else{
      res.sendStatus(200);
    }
    })
  },
  update: function(req,res){
    Player.update({_id:req.params.id}, req.body, function(err,data){
      if(err){
        console.log(err)
        res.status(400).send("Problem updating player.")
      }
       else{
      res.sendStatus(200);
    }
    })
  },
  delete: function(req,res){
    Player.findOne({_id:req.params.id}, function(err, data){
      if(data == null){
        res.status(400).send("No Player found");
      }
      else{
      data.remove();
      res.status(200).send("Player was deleted.");
    }
    })
  },
  show: function(req,res){
    Player.findOne({_id:req.params.id}, function(err, data){
      if(data == null){
        res.status(400).send("No Player found");
      }
      else{
      res.json(data);
    }
    })
  }
}