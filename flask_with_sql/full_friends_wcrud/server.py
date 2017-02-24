from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'freinds_full')
# an example of running a query
print mysql.query_db("SELECT * FROM friend")
app.secret_key = "secret"



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/friends', methods=['POST'])
def create_user():
	valpass = True
	if len(request.form['first']) < 1:
		flash('first name cannot be blank!')
		valpass = False
	if len(request.form['last']) < 1:
		flash('last name cannot be blank!')
		valpass = False
	if len(request.form['email']) < 1:
		flash('email name cannot be blank!')
		valpass = False
	if valpass == False:	
		return redirect('/')	
	else:
		query = "INSERT INTO friend (first_name, last_name, email, create_date) VALUES (:first_name, :last_name, :email, NOW())"	
		data = {
			'first_name': request.form['first'],
			'last_name': request.form['last'],
			'email': request.form['email']
		}
		mysql.query_db(query, data)
		return render_template("friends.html", data = data)


app.run(debug=True)