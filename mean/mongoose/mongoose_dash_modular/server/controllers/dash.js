var mongoose = require('mongoose')


var XmanSchema = new mongoose.Schema({
 name: {type: String, required:true},
 age: {type: Number, required:true },
 power: {type: String, required:true },
 HeroColors: []
})

mongoose.model('Xman', XmanSchema);
var Xman = mongoose.model('Xman')