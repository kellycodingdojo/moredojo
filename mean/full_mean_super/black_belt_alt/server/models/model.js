var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var QuestionSchema = new mongoose.Schema({
  question: {type:String, required: true},
  description: {type:String},
  answers: [{type:Schema.Types.ObjectId, ref: 'Answer'}]
}, {timestamps:true})

mongoose.model('Question', QuestionSchema);

var AnswerSchema = new mongoose.Schema({
  user: {type:String, required: true},
  answer: {type:String, required: true},
  detail: {type:String},
  likes: {type:Number, default:0},
  _question: {type:Schema.Types.ObjectId, ref:'Question'}
}, {timestamps:true})

mongoose.model('Answer', AnswerSchema);
