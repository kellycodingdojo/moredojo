from __future__ import unicode_literals
import re, bcrypt
from django.db import models

class UserManager(models.Manager):
    def login(self, postData):
        error_msgs = []
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        try:
            user = User.objects.get(username=postData['username'])
        except:
            error_msgs.append("Bad Login****!")
            return {'errors':error_msgs}

        if not bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password.encode():
            error_msgs.append("Bad Login****!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            return {'theuser':user.name, 'username':user.username, 'userid':user.id}

    def register(self, postData):
        error_msgs = []
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        date = postData['date']
        if not date:
			error_msgs.append("must  enter date.")

        if len(postData['name']) < 4:
            error_msgs.append("Name is too short!")

        if len(postData['username']) < 4:
            error_msgs.append("username is too short!")

        if len(postData['password']) < 8:
            error_msgs.append("Password is too short!")

        if not postData['password'] == postData['confirm']:
            error_msgs.append("Passwords do not match!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(name=postData['name'], username=postData['username'], date=postData['date'], password=hashed)
            return {'theuser':user.name, 'username':user.username, 'userid':user.id, 'date':user.date}

class ProductManager(models.Manager):
    def add_product(self, postData, userid):
        error_msgs = []
        if len(postData['product_name']) < 3:
            error_msgs.append("Enter Longer Name")
        if error_msgs:
            return {'errors':error_msgs}
        else:
        	user = User.objects.get(id=userid)
        	new_product = Product.objects.create(product_name=postData['product_name'], users=user)
        	return {'userid':user.id, 'product_user':user.id}


class User(models.Model):
    name = models.CharField(max_length=45,null=True)
    username = models.CharField(max_length=45, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Product(models.Model):
	product_name =models.CharField(max_length=255,null=True)
	users = models.ForeignKey(User, related_name="user_key")
	products = models.ForeignKey(User, related_name="product_key", null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ProductManager()

class Wishlist(models.Model):
	wish_users = models.ForeignKey(User, related_name="wish_key")
	wish_products = models.ForeignKey(Product, related_name="wish_product_key", null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)