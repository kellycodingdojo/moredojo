from django.shortcuts import render, redirect, HttpResponse
from models import User, Product, Wishlist
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'main.html')


def register(request):
    if request.method == "POST":
        user = User.objects.register(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('/')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['username'] = user['username']
            request.session['userid'] = user['userid']
            return redirect('/dashboard')

def login(request):
    if request.method == "POST":
        user = User.objects.login(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('/')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['username'] = user['username']
            request.session['userid'] = user['userid']
            return redirect('/dashboard')

def add_item(request):
    return render(request, 'create.html')

def add_product(request):
	  if request.method == "POST":
	    product = Product.objects.add_product(request.POST, request.session['userid'])
	    if 'errors' in product:
	        for error in product['errors']:
	            messages.error(request, error)
	        return redirect('/wish_items/create')
	    else:
	        return redirect('/dashboard')
 

def add_wish(request,id):
	user = User.objects.get(id=request.session['userid'])
	product_wish = Product.objects.get(id = id)
	Wishlist.objects.create(wish_users=user, wish_products=product_wish)
	return redirect('/dashboard')





def dash(request):
	products = Product.objects.filter(users__id = request.session['userid'])
	wish_list = Wishlist.objects.filter(wish_users__id = request.session['userid'])
	others_wish_list = Wishlist.objects.all().exclude(wish_users__id = request.session['userid'])
	context = {
	'products':products,
	'wish_list': wish_list,
	'others_wish_list':others_wish_list
	}
	return render(request, 'dashboard.html',context)


def remove(request,id):
		user = User.objects.get(id =request.session['userid'])
		Wishlist.objects.get(id=id,wish_users=user).delete()
		return redirect('/dashboard')

def delete(request, id):
    Product.objects.get(wish_product_key__id=id).delete()
    return redirect('/dashboard')

def show_product(request, id):
    show_product = Product.objects.get(id=id)
    show_users = User.objects.filter(product_key__wish_product_key__id = id)
    context = {
    'show_product': show_product,
    'show_users': show_users
    }
    return render(request, 'show.html',context)



def logout(request):
    del request.session['theuser']
    del request.session['username']
    del request.session['userid']
    return redirect('/')


# def wishlist(request):
# 	products = Product.objects.all()
# 	context = {
# 	'products':products
# 	}
# 	return redirect('/dashboard',context)