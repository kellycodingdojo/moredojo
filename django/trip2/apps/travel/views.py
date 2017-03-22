from django.shortcuts import render, redirect, HttpResponse
from models import User, Trip 
from django.contrib import messages
# from django.db.models import Count
import datetime


def index(request):
	return render(request, 'main.html')



def display(request):
    travel_list = Trip.objects.all()
    user_list = User.objects.all()
    context = {
        'travel_list': travel_list,
        'user_list': user_list
    }
    return render(request, 'display.html', context)
    

def register(request):
    if request.method == "POST":
        user = User.objects.register(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('/')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['username'] = user['username']
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
            request.session['username'] = user['username']
            request.session['userid'] = user['userid']
            return redirect('/travels')



# def see_book(request, id):
#     book =  Books.objects.get(id=id)
#     context = {
#     'the_book': book,
#     'the_author': Authors.objects.get(id=id),
#     'the_rating': Reviews.objects.filter(book=book)
#     }        
#     return render(request,'book_view.html', context)



def travel_form(request):

	return render(request, 'add.html')

def add_trip(request):
	if request.method == "POST":
		trip_info = Trip.objects.add_trip_model(request.POST, request.session['userid'])
        if 'errors' in trip_info:
            for error in trip_info['errors']:
                messages.error(request, error)
            return redirect('/travels/add')
        else:
            return redirect('/travels')

def logout(request):
    del request.session['theuser']
    del request.session['userid']
    return redirect('/')

def destination(request,id):
    travel_list = Trip.objects.get(id=id)
    others = User.objects.filter(jointravels__id=id) # this is a many to many
    print id
    context = {
        'travel_list': travel_list ,
        'others': others 
    }
    return render(request, 'destination.html', context)



def travel_dash(request):
    travel_list = Trip.objects.filter(user__id = request.session['userid']) #these are foriegn keys
    trips_joined = Trip.objects.filter(join__id = request.session['userid'])
    others_list = Trip.objects.all().exclude(user__id = request.session['userid']).exclude(join__id = request.session['userid'])
    context = {
        'joined':trips_joined,
        'travel_list': travel_list,
        'others_list': others_list
    }
    return render(request, 'travels.html', context)

def joins(request,id): 
    trip =Trip.objects.get(id=id) # trip is holding the id of the trip that you clicked.
    print trip.id
    user = User.objects.get(id = request.session['userid']) # is holding the id of the current user.
    trip.join.add(user) # using the forgein key to take the trip id and add your user id to it. 
    return redirect('/travels')


