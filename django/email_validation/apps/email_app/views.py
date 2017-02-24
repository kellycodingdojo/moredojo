from django.shortcuts import render, redirect, HttpResponse
import datetime
from models import Email_val
from django.contrib import messages

 

def index(request): 
	email = Email_val.objects.all()
	context = {
		'email': email
	}
	return render(request, 'index.html', context)



def validate(request):
	if request.method == "POST":
		print request.POST
		good_email = Email_val.objects.validate_email(request.POST)
		if 'errors' in good_email:
			for fails in good_email['errors']:
				messages.error(request, fails)
				return redirect('/')
		if 'theinfo' in good_email:
			messages.success(request, good_email['theinfo'].email)	
		return redirect('/success')

def results(request):
	email = Email_val.objects.all()
	context = {
		'email':email
	}
	return render(request, 'success.html', context)	