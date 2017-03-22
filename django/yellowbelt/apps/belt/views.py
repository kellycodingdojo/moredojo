from django.shortcuts import render, redirect, HttpResponse
from models import User, Quote, Fav
from django.contrib import messages
from django.db.models import Count
# import datetime

def index(request):
	return render(request,'main.html')

def main(request):
	return render(request,'main.html')


def display(request):
    quote_list = Quote.objects.all()
    user_list = User.objects.all()
    fav_list = Fav.objects.all()
    context = {
        'quote_list': quote_list,
        'user_list': user_list,
        'fav_list': fav_list
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
            request.session['alias'] = user['alias']
            request.session['userid'] = user['userid']
            return redirect('/quotes')

def login(request):
    if request.method == "POST":
        user = User.objects.login(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('/')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['alias'] = user['alias']
            request.session['userid'] = user['userid']
            return redirect('/quotes')


def quotes(request):
    quote_list = Quote.objects.exclude(user__id = request.session['userid']).exclude(fav__fav_user__id=request.session['userid']) # this is broken it does not exclude your favs. 
    fav_list = Fav.objects.filter(fav_user__id=request.session['userid'])# this may be fixed, this is broken it displays all favs. 
    context = {
    'quote_list':quote_list,
    'fav_list':fav_list,
    }
    return render(request, 'quotes.html', context)

def add_quote(request):
	if request.method == "POST":
		new_quote = Quote.objects.add_quote(request.POST, request.session['userid'])
		if 'errors' in new_quote:
			for error in new_quote['errors']:
				messages.error(request, error)
			return redirect('/quotes')
		else:
			return redirect('/quotes')



def user_gen(request,id):
	stuff = User.objects.get(id=id)
	context = {
	'user': stuff,
	'quote': Quote.objects.filter(user=stuff)
	}
	context['total_reviews']=Quote.objects.annotate(count=Count('quote')).filter(user__id=context['user'].id)
	return render(request, 'users.html', context)

def add_fav(request,id):
	user = User.objects.get(id=request.session['userid'])
	favquote = Quote.objects.get(id = id)
	print favquote.id
	Fav.objects.create(fav_user=user, fav_quote=favquote)
	return redirect('/quotes')


def delete(request, id):
    Fav.objects.get(id=id).delete()
    return redirect('/quotes')


def logout(request):
    del request.session['theuser']
    del request.session['alias']
    del request.session['userid']
    return redirect('/')


