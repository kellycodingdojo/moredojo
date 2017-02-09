from flask import Flask, redirect, render_template, session, request, flash
app = Flask(__name__)
# You need to set a secret key to use the session module
# The secret key is used to encrypt and decrypt the user's session id from the browser's cookie
# In practice this will be a long string of random, cryptographically secure characters
# http://flask.pocoo.org/docs/0.12/quickstart/#sessions
app.secret_key = "IsThisEasyMode"

@app.route('/')
def index():
	# We need to initialize the key 'user' in the session if it's not already set
	# Understanding the dictionary data structure in Python is important!
	# https://docs.python.org/2/tutorial/datastructures.html#dictionaries
	# Section "Sessions" in the Flask Fundamentals tab of the learning platform
	if 'user' not in session:
		session['user'] = "Kevin"
	return render_template('index.html')


@app.route('/comments', methods=['POST'])
def check():
	# has_errors is a boolean to decide if the user input is good or bad. If we fail validation, we switch the value to true
	has_errors = False
	# The form data sent along with the request is inside of request.form. We can access input values using the dictionary syntax
	if len(request.form['content'])<2:
		flash('Too short')
		has_errors = True
	# We used the values inside of a hidden input 'form_name' to determine which form the user filled out. Check out the html.
	if request.form['form_name'] == "wrong_form":
		flash("You filled out the wrong form, dummy")
		has_errors = True
	if has_errors == True:
		# If the input is bad, then you redirect back to the route that renders the form
		return redirect('/')
	else:
		# If it is good, then you redirect to a different route
		return redirect('/success')


@app.route('/success')
def success():
	return render_template('success.html')

app.run(debug=True)