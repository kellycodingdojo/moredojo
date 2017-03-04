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
    user_list = User.objects.all().exclude(id = request.session['userid'])
    context = {
        'friend_list': friend_list,
        'user_list': user_list
    }
    return render(request, 'friends.html', context)


# def add_friend(request,id): 
# 	user = User.objects.get(id=request.session['userid']) #user is grabbing the current users id. 
# 	newfriend = Friend.objects.add_friend(friend_name= )
# 	user.joins = newfriend
# 	user.save()
# 	return redirect('/friends')

# def add_friend(request,id): 
# 	user = User.objects.get(id=request.session['userid'])#user is grabbing the current users id. 
# 	print user.id 
# 	newfriend = User.objects.get(id =id ) # grab the id of who you want to add as friend.
# 	print newfriend.id
# 	print Friend
# 	print Friend.objects
# 	guy = Friend.objects
# 	guy.joins.add(id=user,friend_name=newfriend.name)
# 	return redirect('/friends')

def add_friend(request,id): 
	user = User.objects.get(id=request.session['userid'])#user is grabbing the current users id. 
	print user.id 
	newfriend = User.objects.get(id =id ) # grab the id of who you want to add as friend.
	print newfriend.id 
	Friend.objects.create(users=user, friends=newfriend)
	return redirect('/friends')

# def add_friend(request,id): 
# 	user = User.objects.get(id=request.session['userid']) #user is grabbing the current users id. 
# 	newfriend = User.objects.get(id =id ) # grab the id of who you want to add as friend. 
# 	friends = Friend.objects.add(id=user, friend_name=newfriend.name)
# 	return redirect('/friends')
	
# #ype object 'User' has no attribute 'joins'
# #'Manager' object has no attribute 'add'

# def joins(request,id): 
#     trip =Trip.objects.get(id=id)
#     print trip.id
#     user = User.objects.get(id = request.session['userid'])
#     trip.join.add(user)
#     return redirect('/travels')

# def add_friend(request,id):
# 	user = User.objects.get(id = request.session['userid'])
# 	friends = Friend(user=request.user, friend= user)
# 	return redirect('/friends')

# def add_friend(request,id):
# 	user = User.objects.get(id = request.session['userid'])
# 	friend_manage = add_friend(friend_name=user.name)
# 	friend_manage.save()
# 	return redirect('/friends')

# def add_friend(request,id):
# 	print id
# 	user = User.objects.get(id = request.session['userid'])
# 	Friend.users.add_friend(user)
# 	return redirect('/friends')

# def add(request):
#         user = {'user': User.objects.get(id = request.session['userid'])}
#         book = {'book': Books.objects.get(id=postData['id'])}
#         Reviews.objects.create(review=postData['review'], rating=postData['rating'], book=book['book'], user=user['user'])
#         return

# def add(request):
#     context = {'freinds':Friends.objects.all()}
#     return render(request, 'beltrev/add.html', context)