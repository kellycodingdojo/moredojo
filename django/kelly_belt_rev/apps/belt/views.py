from django.shortcuts import render, redirect
from models import User, Books
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def books(request):
    return render(request, 'books.html')

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
		new_product = Books.objects.add_book(request.POST)
		if 'errors' in new_product:
			for error in new_product['errors']:
				messages.error(request, error)
			return redirect('/books')
		else:
			return render(request,'book_view.html')

def see_book(request):
    return render(request, 'book_view.html')

# def add_book(request):
#     if request.method == "POST":
#     	print 123
#         book = Books.objects.add_book(request.POST)
#         restr = '/books/add' + str(book['bookid'])
#         return redirect(restr)