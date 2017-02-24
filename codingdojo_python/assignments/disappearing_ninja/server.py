from flask import Flask, render_template, redirect, request, session, flash, url_for
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ninja')
def getall():
	ninjalist = ['donatello','leonardo','michelangelo','raphael']
	return render_template('ninja.html', listofninjas = ninjalist)

@app.route('/ninja/<color>')
def getcolor(color):
	if color == "red":
		ninjalist = ["raphael"]

	elif color == "orange":
		ninjalist = ["michelangelo"]
	
	elif color == "purple":
		ninjalist = ["donatello"]

	elif color == "blue":
		ninjalist = ["leonardo"]

	else:
		ninjalist = ['notapril']

	return render_template('ninja.html', listofninjas = ninjalist)
     
app.run(debug=True)