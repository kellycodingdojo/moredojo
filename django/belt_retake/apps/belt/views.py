from django.shortcuts import render, redirect, HttpResponse
from models import User, Friend
from django.contrib import messages


# Create your views here.
def forward(request):
    return render(request, 'main.html')

def main(request):
    return render(request, 'main.html')

def home(request):
    return redirect(request, 'friends.html')

def logout(request):
    del request.session['theuser']
    del request.session['userid']
    return redirect('/')

def display(request):
	friend_list = Friend.objects.all()
	user_list = User.objects.all()
	context = {
		'friend_list': friend_list,
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
            request.session['alias'] = user['alias']
            request.session['userid'] = user['userid']
            return redirect('/friends')

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
            return redirect('/friends')

def friends(request):
	friend_list = Friend.objects.all()
	user_list = User.objects.all()
	context = {
		'friend_list': friend_list,
		'user_list': user_list
	}
	return render(request, 'friends.html', context)


def add_friend(request,id): 
    friend = Friend.objects.get(id=id)
    print friend.id
    user = User.objects.get(id = request.session['userid'])
    users.friend.add(user)
    return redirect('/friends')

