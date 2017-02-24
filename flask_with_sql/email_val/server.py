from flask import Flask, render_template, redirect, request, session, flash

# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
import re
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email')
# an example of running a query
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"


@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
    	query = "INSERT INTO email_table (email) VALUES (:email)" #so you are having duplicate emails. 
    	data = {'email': request.form['email']}
    	mysql.query_db(query, data)

    	query_all = "SELECT * FROM email_table"
    	final = mysql.query_db(query_all)
    	return render_template("success.html",data=data,final=final)

    return redirect('/')

# @app.route('/process', methods=['POST'])
# def create():
#     # Write query as a string. Notice how we have multiple values
#     # we want to insert into our query.
#     query = "INSERT INTO email (email) VALUES (:email)"
#     # We'll then create a dictionary of data from the POST data received.
#     data = {
#              'email': request.form['email'],  
#            }
  
#     mysql.query_db(query, data)
#     return render_template("success.html")





app.run(debug=True)