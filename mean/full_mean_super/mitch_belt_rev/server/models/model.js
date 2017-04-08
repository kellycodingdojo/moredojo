var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var UserSchema = new mongoose.Schema({
  name: {type:String, required: true, unique: true},
  topics: [{type:Schema.Types.ObjectId, ref: 'Topic'}],
  posts: [{type:Schema.Types.ObjectId, ref: 'Post'}],
  comments: [{type:Schema.Types.ObjectId, ref:'Comment'}]
}, {timestamps:true})

mongoose.model('User', UserSchema);

var TopicSchema = new mongoose.Schema({
  topic: {type:String, required: true},
  description: {type:String, required: true},
  category:{type:String, required:true},
  _user: {type:Schema.Types.ObjectId, ref: 'User'},
  posts: [{type:Schema.Types.ObjectId, ref: 'Post'}],
}, {timestamps:true})

mongoose.model('Topic', TopicSchema);

var PostSchema = new mongoose.Schema({
  post: {type:String, required: true},
  upvotes: {type:Number, default: 0},
  downvotes: {type:Number, default: 0},
  _user: {type:Schema.Types.ObjectId, ref: 'User'},
  _topic: {type:Schema.Types.ObjectId, ref: 'Topic'},
  comments: [{type:Schema.Types.ObjectId, ref: 'Comment'}]
}, {timestamps:true})

mongoose.model('Post', PostSchema);

var CommentSchema = new mongoose.Schema({
  comment: {type:String, required: true},
  _user: {type:Schema.Types.ObjectId, ref:'User'},
  _post: {type:Schema.Types.ObjectId, ref:'Post'}
}, {timestamps:true})

mongoose.model('Comment', CommentSchema);
