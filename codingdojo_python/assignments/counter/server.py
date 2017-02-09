from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'secret'

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1


@app.route('/')

def counter():
    sumSessionCounter()

    return render_template('counter.html')

@app.route('/counter', methods=['post'])

def clear():

    session['counter'] = 0
    return redirect('/')

@app.route('/two', methods=['post'])

def two():
    session['counter'] += 1
    return redirect('/')


@app.route('/double', methods=['post'])

def double():
    session['counter'] *= 2 
    session['counter'] -= 1
    return redirect('/')

app.run(debug=True)






