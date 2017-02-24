from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=['POST'])
def create_user():
  if len(request.form['name']) < 1:
    flash('name cannot be empty')
    error_name = False
  else:
    name = request.form['name']
    error_name = True

  if len(request.form['email']) < 8 or len(request.form['email']) > 15:
    flash('email must be longer')
    error_email = False
  else:
    email = request.form['email']
    error_email = True  


  if error_name == False or error_email == False:
    return redirect('/')
  else:  
    return render_template('users.html', name = name, email = email)  
    # session['email'] = request.form['email']
    # session['location'] = request.form['location']
    # session['language'] = request.form['language']
     #redirects back to the '/' route
  #return render_template('users.html',name = name, email = email, location = location, language = language)
   

# @app.route('/')
# def show_user():
#   #return render_template('users.html', name=session['name'], email=session['email'],location=session['location'],language=session['language'])
# 	return render_template('users.html')






app.run(debug=True) # run our server