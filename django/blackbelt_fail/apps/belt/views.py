from django.shortcuts import render, redirect
from models import User, Travels
from django.contrib import messages



def main(request):
    return render(request, 'main.html')


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


def add(request):
	return render(request, 'add.html')
		

def travels(request):
	travel_goods = Travels.objects.all()
	the_goods = User.objects.all()
	context = {
				'everthing': travel_goods,
				'everyone': the_goods,
			}
	return render(request, 'travels.html', context)

def logout(request):
    del request.session['theuser']
    del request.session['userid']
    return redirect('/')

def add_trip(request):
	if request.method == "POST":
		user = Travels.objects.add(request.POST)
		if 'errors' in user:
			for error in user['errors']:
				messages.error(request, error)
				return redirect('/')
		if 'trip_id' in user:
			request.session['trip_dest'] = user['trip_dest']
			request.session['trip_id'] = user['trip_id']
			return redirect('/travels')
	
   
