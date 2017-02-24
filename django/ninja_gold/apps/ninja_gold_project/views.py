from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'activities' not in request.session:
		request.session['activities'] = []
	return render(request, 'index.html')
	

def get_money(request):
	if request.POST['building'] == 'farm':
		num = random.randrange(10,20)
		gold = request.session['gold']
		request.session['gold'] += num
		request.session['activities'].insert(0,'earned ' + str(num) + ' golds from the farm ' + 'you have ' + str(gold) + ' total @ ' + str(datetime.datetime.now()) )

	if request.POST['building'] == 'cave':
		num = random.randrange(5,10)
		gold = request.session['gold']
		request.session['gold'] += num
		request.session['activities'].insert(0,'earned ' + str(num) + ' golds from the cave ' + 'you have ' + str(gold) + ' total @ ' + str(datetime.datetime.now()))

	if request.POST['building'] == 'house':
		num = random.randrange(2,5)
		gold = request.session['gold']
		request.session['gold'] += num
		request.session['activities'].insert(0,'earned ' + str(num) + ' golds from the house ' + 'you have ' + str(gold) + ' total @ ' + str(datetime.datetime.now()))
	
	elif request.POST['building'] == 'casino':
		if request.session['gold'] < 50:
			request.session['activities'].insert(0,'your broke go away @ ' + str(datetime.datetime.now()) )
			request.session.modified = True
			return redirect('/')
		num = random.randrange(1,50)
		halfy = random.randrange(0,2)
		if halfy == 0: 
			request.session['gold'] -= num
			request.session['activities'].insert(0,"loss " + str(num) + " golds from the casino @ " + str(datetime.datetime.now()))   
		else:
			request.session['gold'] += num  
			request.session['activities'].insert(0,"earned " + str(num) + " golds from the casino @ " + str(datetime.datetime.now()))
	request.session.modified = True
	return redirect('/')	


def resetnow(request):
    if request.POST['reset'] == 'nomore':
        request.session['gold'] = 0
    return redirect('/')	

def goaway(request):
	if request.POST['form_reset'] == 'non':
		request.session['activities'] = []
	else:
		request.session['activities'].insert(0, "Nothing to Delete")
	return redirect('/')  