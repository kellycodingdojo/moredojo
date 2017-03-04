from django.shortcuts import render, redirect, HttpResponse
from .models import User, Travel
from django.contrib import messages

def index(request):
	return render(request, 'bp_app/index.html')

def register(request):
	if request.method == "POST":
		user = User.objects.register(request.POST)
		if 'errors' in user:
			for error in user['errors']:
				messages.error(request, error)
			return redirect('/')
		if 'theuser' in user:
			request.session['theuser'] = user['theuser']
			request.session['userid'] = user['userid']
			return redirect('/travels')

def login(request):
	if request.method == "POST":
		user = User.objects.login(request.POST)
		if 'errors' in user:
			for error in user['errors']:
				messages.error(request, error)
				return redirect('/')
		if 'theuser' in user:
			request.session['theuser'] = user['theuser']
			request.session['userid'] = user['userid']
			return redirect('/travels')

def home(request):
    return redirect('/travels')

def logout(request):
    del request.session['theuser']
    del request.session['userid']
    return redirect('/main')

def add(request):
	return render(request, 'bp_app/add.html')

def added(request):
	if request.method == 'POST':
		travel = Travel.objects.addtravel(request.POST, request.session['userid'])
		if 'errors' in travel:
			for error in travel['errors']:
				messages.error(request,error)
			return redirect ('/travels/add')
		if 'travelid' in travel:
			return redirect('/travels')

def travels(request):
	travels= Travel.objects.filter(user__id = request.session['userid']) | Travel.objects.filter(join__id= request.session['userid'])
	other_travels = Travel.objects.exclude(user__id = request.session['userid']) & Travel.objects.exclude(join__id = request.session['userid'])
	context={
		'travels': travels,
		'other_travels': other_travels
	}
	return render(request, 'bp_app/travels.html', context)

def joins(request,id):
	trip = Travel.objects.get(id= id)
	user_id = User.objects.get(id= request.session['userid'])
	trip.join.add(user_id)

	return redirect('/travels')

def destination(request,id):
	trip = Travel.objects.get(id=id)
	other_users = User.objects.filter(jointravels__id=id)
	context={
		'trip': trip,
		'other_users': other_users
	}
	return render(request, 'bp_app/destination.html', context)



