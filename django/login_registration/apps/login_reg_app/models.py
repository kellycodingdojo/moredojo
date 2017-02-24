from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Manager(models.Manager):
	def validate(self, post_data):
		error_msgs = []
		if len(post_data['email']) < 4:
			error_msgs.append('email is too short')
		if Validation.objects.filter(email = post_data['email']).exists():
			error_msgs.append('email already in database')	
		if not EMAIL_REGEX.match(post_data['email']):
			error_msgs.append(' email not valid')
		if len(post_data['first']) < 4:
			error_msgs.append('First name is too short')
		if len(post_data['last']) < 4:
			error_msgs.append('Last name is too short')	
		if post_data['password'] != post_data['confirm']:
			error_msgs.append('Passwords dont match')

		if error_msgs:
			return{'errors':error_msgs}
		else:
			encoded = post_data['password'].encode('utf-8')
			get_info = Validation.objects.create(
				first = post_data['first'],
				last = post_data['last'],
				email = post_data['email'],
				password = bcrypt.hashpw(encoded, bcrypt.gensalt())
			)	
			return {'theinfo':get_info}


	def login(self,post_data):
		error_msgs = []
		if Validation.objects.filter(email=post_data['email']):
			hashed = Validation.objects.get(email=post_data['email']).password
			hashed = hashed.encode('utf-8')
			user_pass = post_data['password'].encode('utf-8')
			if bcrypt.hashpw(user_pass,hashed) == hashed:
				print "Hey congrats you where able to remeber your password!"
				user = Validation.objects.get(email=post_data['email'])
				return{'thelogin':user } 
			else:
				print "Wrong Password"
				error_msgs.append('Invalid login!')
				return {'errors':error_msgs}
		else:
			print "bad email"
			error_msgs.append('Try Again Fool')
			return {'errors':error_msgs}

	

class Validation(models.Model):
	email = models.CharField(max_length=50,unique=True)
	first = models.CharField(max_length=50)
	last = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	objects = Manager()
