from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def get_random():
    if not session.has_key('randi'):
        session['randi'] = random.randrange(0,101)
    return render_template('guess.html')  


@app.route('/play', methods=['POST'])
def play():
    num = int(request.form['num'])
    win = ''
    if num == session['randi']:
        win = "yes"
    elif num > session['randi']:
        win = "high"
    elif num < session['randi']:
        win ='low'

    return render_template('guess.html', win = win)   

@app.route('/guess', methods=['POST'])
def again():
    session.pop('randi')
    return redirect('/')      

app.run(debug=True)






