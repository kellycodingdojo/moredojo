var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var UserSchema = new mongoose.Schema({
  name: {type:String, required: true, unique: true},
  questions: [{type:Schema.Types.ObjectId, ref: 'Question'}],
  answers: [{type:Schema.Types.ObjectId, ref: 'Answer'}],
}, {timestamps:true})

mongoose.model('User', UserSchema);

var QuestionSchema = new mongoose.Schema({
  question: {type:String, required: true},
  description: {type:String},
  _user: {type:Schema.Types.ObjectId, ref: 'User'},
  _answer: [{type:Schema.Types.ObjectId, ref: 'Answer'}],
}, {timestamps:true})

mongoose.model('Question', QuestionSchema);

var AnswerSchema = new mongoose.Schema({
  answer: {type:String, required: true},
  description: {type:String},
  likes: {type:Number, default: 0},
  _user: {type:Schema.Types.ObjectId, ref: 'User'},
  _question: {type:Schema.Types.ObjectId, ref: 'Question'},
}, {timestamps:true})

mongoose.model('Answer', AnswerSchema);