from django.shortcuts import render, redirect
import random, string


def create(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    characters = ['A', 'B', 'C', 'D', 'Z', 'Y', '1', '2', '7', '3', '6']
    randword = ''
    for blah in range(0, 14):
        idx = random.randint(0, 10)
        randword += characters[idx]
    request.session['word'] = randword
    request.session['attempt'] = request.session['attempt'] + 1
    return redirect('/')

def index(request):
	return render(request,'index.html')

