from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    if not session.has_key('gold'):  # for future ref-- if not 'your_key' in session
        session['gold'] = 0
    if not session.has_key('activities'):
        session['activities'] = []
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def get_money():
    if request.form['building'] == 'farm':
        num = random.randrange(10,20)
        session['gold'] += num
        session['activities'].append(" earned" + str(num) + "golds from the farm")

    elif request.form['building'] == 'cave':
        num = random.randrange(5,10)
        session['gold'] += num 
        session['activities'].append(" earned" + str(num) + "golds from the cave")

    elif request.form['building'] == 'house':
        num = random.randrange(2,5)
        session['gold'] += num
        session['activities'].append(" earned" + str(num) + "golds from the house")

    elif request.form['building'] == 'casino':
        if session['gold'] < 50:
            session['activities'].append('your broke go away')
            return redirect('/')
        num = random.randrange(0,50)
        halfy = random.randrange(0,2)
        if halfy == 0: 
            session['gold'] -= num
            session['activities'].append(" loss" + str(num) + "golds from the casino")   
        else:     
            session['gold'] += num  
            session['activities'].append(" earned" + str(num) + "golds from the casino")   

    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetnow():
    if request.form['reset'] == 'nomore':
        session['gold'] = 0
    return redirect('/')




@app.route('/form_reset', methods=['POST'])
def goaway():
    del session['activities'] 
    return redirect('/')


app.run(debug=True)



# add reset and color code win/loss results. 



