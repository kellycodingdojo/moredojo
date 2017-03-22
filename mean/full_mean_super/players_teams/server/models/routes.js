var mongoose = require('mongoose')

var Schema = mongoose.Schema;

var PlayerSchema = new mongoose.Schema({
	player_name: {type:String, required: true},
	player_team:{type:Schema.Types.ObjectId, ref:'Team'}
}, {timestamps:true})

mongoose.model('Player', PlayerSchema)


var TeamSchema = new mongoose.Schema({
	_player:{type: Schema.Types.ObjectId, ref:'Player'},
	team_name: {type:String, required: true}
}, {timestamps:true})

mongoose.model('Team', TeamSchema)