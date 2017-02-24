from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
  if len(request.form['name']) < 1:
    flash('Name cannot be empty') # just pass a string to the flash function
  else:
    flash("Success! Your name is {}".format(request.form['name'])) # just pass a string to the flash function
  return redirect('/') # either way the application should return to the index and display the message

app.run(debug=True)







# {% with messages = get_flashed_messages() %}
# The with messages here helps us declare a variable in our template that we can use within a specific scope.
# {% if messages %}
# Check if there are even any messages that came back from the get_flashed_messages() function
# {% for message in messages %}
# Loop through all messages
# <p>{{message}}</p>
# Print the messages one by one each in a paragraph tag
