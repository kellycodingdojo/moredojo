from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   session['location'] = request.form['location']
   session['language'] = request.form['language']
   # redirects back to the '/' route
   # return render_template('users.html',name = name, email = email, location = location, language = language)
   return redirect('/show')

@app.route('/show')
def show_user():
  #return render_template('users.html', name=session['name'], email=session['email'],location=session['location'],language=session['language'])
	return render_template('users.html')






app.run(debug=True) # run our server