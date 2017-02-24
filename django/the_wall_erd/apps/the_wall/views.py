from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

def index(request):
	return render(request, 'index.html')