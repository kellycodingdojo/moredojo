from django.shortcuts import render, redirect, HttpResponse
from models import Validation
from django.contrib import messages
 


def index(request):
	return render(request, 'index.html')

def register(request):
	if request.method == "POST":
		print request.POST
		good_info = Validation.objects.validate(request.POST)
		if 'errors' in good_info:
			for fails in good_info['errors']:
				print fails
				messages.error(request, fails)
			return redirect('/')
		if 'theinfo' in good_info:
			messages.success(request, ' Successfully registered', good_info['theinfo'].email)	
	return render(request, 'success.html')


def login(request):
	if request.method =="POST":
		print request.POST
		good_login = Validation.objects.login(request.POST)
		if 'errors' in good_login:
			for fails in good_login['errors']:
				print fails
				messages.error(request, fails)
			return redirect('/')
		if 'thelogin' in good_login:
			request.session['name'] = good_login['thelogin'].first
			print request.session['name']
			messages.success(request, "Successfully logged in " + good_login['thelogin'].first)
			getall = Validation.objects.all()
			context = {
				'everyone': getall
			}
		return render(request, 'success.html', context)
