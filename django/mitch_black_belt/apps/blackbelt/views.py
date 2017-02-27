from django.shortcuts import render, redirect, HttpResponse
from models import User, Trip
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'blackbelt/index.html')

def register(request):
    if request.method == "POST":
        user = User.objects.register(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('/')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['user_name'] = user['user_name']
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
            request.session['user_name'] = user['user_name']
            request.session['userid'] = user['userid']
            return redirect('/travels')

def dash(request):
    context = {'usertrips':Trip.objects.filter(users__id=request.session['userid']),
    'othertrips':Trip.objects.exclude(users__id=request.session['userid'])}
    return render(request, 'blackbelt/travels.html', context)

def add_travel(request):
    return render(request, 'blackbelt/add_travels.html')

def added(request):
    if request.method == "POST":
        trip = Trip.objects.new_trip(request.POST)
        if 'errors' in trip:
            for error in trip['errors']:
                messages.error(request, error)
            return redirect('/travels/add')
        else:
            return redirect('/travels')

def home(request):
    return redirect('/travels')

def travel_plan(request, id):
    context = {'plan': Trip.objects.get(id=id)}
    context['otherusers'] = User.objects.filter(user_trips__id=context['plan'].id).exclude(creator__id=context['plan'].id)
    return render(request, 'blackbelt/plan.html', context)

def logout(request):
    del request.session['userid']
    del request.session['theuser']
    del request.session['user_name']
    return redirect('/')

def join(request, id):
    trip = Trip.objects.get(id=id)
    user = User.objects.get(id=request.session['userid'])
    trip.users.add(user)
    return redirect('/travels')

def delete(request):
    User.objects.all().delete()
    Trip.objects.all().delete()
    return redirect('/')
