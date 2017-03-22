var mongoose = require('mongoose')
var Xman = mongoose.model('Xman');

var myControl = require('./../controllers/controllers.js')

module.exports = function(app){

	app.get('/',myControl.route)

	app.get('/hero/new',myControl.render)

	app.get('/hero/:id', myControl.show)

	app.get('/hero/edit/:id', myControl.edit)

	app.post('/hero', myControl.newhero)

	app.post('/hero/:id', myControl.update)

	app.post('/hero/delete/:id', myControl.delete)
}