from django.shortcuts import render, redirect, HttpResponse
from models import Course
import datetime

def create(request):
	if request.method =='POST':
		Course.objects.create(name=request.POST['name'],
		comment=request.POST['comment']) 
	return redirect('/')


def index(request):
	all_course = Course.objects.all()
	context = {
	'the_goods':all_course
	}
	return render(request, 'index.html', context)

def delete(request,id):
	all_course = Course.objects.get(id=id)
	context = {
	'which':all_course
	}
	
	return render(request, 'sure.html', context)

def yes(request,id):
	Course.objects.get(id=id).delete() 
	return redirect('/')