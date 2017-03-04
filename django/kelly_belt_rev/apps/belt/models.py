from __future__ import unicode_literals
from django.db import models
import bcrypt, re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):
    def login(self, postData):
        error_msgs = []
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        try:
            user = User.objects.get(email=postData['email'])
        except:
            error_msgs.append("Invalid user!")
            return {'errors':error_msgs}

        if not bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password.encode():
            error_msgs.append("Wrong Password!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            return {'theuser':user.first, 'alias':user.alias, 'userid':user.id}

    def register(self, postData):
        error_msgs = []
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        try:
            if User.objects.get(email=postData['email']):
                error_msgs.append("Email already in use!")
        except:
            pass

        if len(postData['first']) < 4:
            error_msgs.append("first is too short!")

        if len(postData['alias']) < 4:
            error_msgs.append("alias is too short!")

        if not email_regex.match(postData['email']):
            error_msgs.append("Invalid email!")

        if len(postData['password']) < 8:
            error_msgs.append("Password is too short!")

        if not postData['password'] == postData['confirm']:
            error_msgs.append("Passwords do not match!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(
        	email=postData['email'],
        	first=postData['first'],
        	alias=postData['alias'],
        	password=hashed)
            return {'theuser':user.first, 'alias':user.alias, 'userid':user.id}

	

class User(models.Model):
	email = models.CharField(max_length=50,unique=True)
	first = models.CharField(max_length=50)
	alias = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()


class BookManager(models.Manager):
	def add_book(self, postData, userid):
		error_msgs = []
		try:
			Books.objects.get(title=postData['title'])
			error_msgs.append("That book already exists.")		
		except:
			pass
		if len(postData['title']) < 2:
			error_msgs.append("Must enter title!")
			print "2"
		if len(postData['review']) < 5:
			error_msgs.append("Must enter review")
			print "3"
		if error_msgs:
			return {'errors':error_msgs}
		else:
			author = Authors.objects.create(name=postData['new_author'])
			book = Books.objects.create(title=postData['title'], author=author)
			Reviews.objects.create(
			review=postData['review'], 
			rating=int(postData['rating']), 
			book=Books.objects.get(id=book.id),
			user=User.objects.get(id=userid))
			return {'bookid':book.id}

class Authors(models.Model):
	name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
               
class Books(models.Model):
	title = models.CharField(max_length=50,unique=True)
	author = models.CharField(max_length=50)
	review = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BookManager()

class ReviewManager(models.Manager):
    def add(self, postData, userid):
        user = User.objects.get(id=userid)
        book = Books.objects.get(id=int(postData['id']))
        Reviews.objects.create(
	        review=postData['review'],
	        rating=postData['rating'],
	        book=book,
	        user=user)
        return



class Reviews(models.Model):
    review = models.TextField()
    rating = models.CharField(max_length=1)
    book = models.ForeignKey(Books, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

