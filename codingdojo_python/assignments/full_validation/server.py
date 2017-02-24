# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
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

    if len(request.form['first']) < 1:
    	flash('Name cannot be blank')   
    elif not request.form['first'].isalpha():
    	flash('must not contain numbers')	

    if len(request.form['last']) < 1:
    	flash('Name cannot be blank')   
    elif not request.form['last'].isalpha():
    	flash('must not contain numbers')
  
    if len(request.form['password']) < 1:
    	flash('Name cannot be blank')   
    elif request.form['password'] < 8:
    	flash('must be longer then 8 characters')
    
    if request.form['confirm'] != request.form['password']:
    	flash('passwords do not match')   
    else:
    	flash('success!')	



    return redirect('/')
app.run(debug=True)