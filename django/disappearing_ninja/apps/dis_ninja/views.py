from django.shortcuts import render, redirect, HttpResponse

def create(request):
	print "dljshdfjklds"
	return render(request,'index.html')


def show(request, id):
	context = {
		'key' : id,
	}
	return render(request,'index.html', context)

def ninja(request):
	context = {
		'key' : None,
	}
	return render(request,'index.html', context)
