from django.shortcuts import render, redirect
import random, string


def create(request):
    return render(request,'index.html')

def index(request):
	return render(request,'index.html')
	
def submit_form(request):
	if 'num_clicks' not in request.session:
		request.session['num_clicks'] = 0
	request.session['name'] = request.POST['first']
	request.session['city'] = request.POST['city']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	request.session['num_clicks'] = request.session['num_clicks'] + 1
	return render(request,'result.html')

