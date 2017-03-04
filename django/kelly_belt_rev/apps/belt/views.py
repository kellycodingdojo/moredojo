from django.shortcuts import render, redirect
from models import User, Books, Authors, Reviews
from django.contrib import messages
from django.db.models import Count


def index(request):
    return render(request, 'index.html')

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
            return redirect('/books')

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
            return redirect('/books')

# def add_book(request,id):
# 	book_info = Books.objects.get(id=id)
# 	context = {
# 	'book_info': book_info
# 	}
# 	return render(request,'add.html', context)

def add(request):
    return render(request, 'add.html')

def add_book(request):
	if request.method == "POST":
		new_product = Books.objects.add_book(request.POST, request.session['userid'])
		if 'errors' in new_product:
			for error in new_product['errors']:
				messages.error(request, error)
			return redirect('/books/add')
		else:
			return redirect('/books/'+ str(new_product['bookid']))

def see_book(request, id):
	book =  Books.objects.get(id=id)
	context = {
	'the_book': book,
	'the_author': Authors.objects.get(id=id),
	'the_rating': Reviews.objects.filter(book=book)
	}        
	return render(request,'book_view.html', context)
	

def add_review(request):
	if request.method == "POST":
		Reviews.objects.add(request.POST, request.session['userid'])
		return redirect('/books/' + str(request.POST['id']))


def user_info(request, id):
	context = {'user':User.objects.get(id=id)}
	context['total_reviews']=Reviews.objects.annotate(count=Count('review')).filter(user__id=context['user'].id)
	return render(request, 'users.html', context)

def books(request):
	context = {
	'top_three':Reviews.objects.all().order_by('-created_at')[:3],
	'all_books':Books.objects.all()
	}
	return render(request, 'books.html',context)

def delete(request, id, book_id):
    Reviews.objects.get(id=id).delete()
    return redirect('/books/'+ book_id)