from __future__ import unicode_literals
from django.db import models
import bcrypt
from datetime import time, datetime, date



# Create your models here.
class UserManager(models.Manager):
    def login(self, postData):
        error_msgs = []
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        try:
            user = User.objects.get(username=postData['username'])
        except:
            error_msgs.append("Invalid login!")
            return {'errors':error_msgs}

        if not bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password.encode():
            error_msgs.append("Invalid login!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            return {'theuser':user.name, 'username':user.username, 'userid':user.id}

    def register(self, postData):
        error_msgs = []

        try:
            if User.objects.get(username=postData['username']):
                error_msgs.append("Username already exists")
        except:
            pass

        if len(postData['name']) < 4:
            error_msgs.append("first is too short!")

        if len(postData['username']) < 4:
            error_msgs.append("username is too short!")

        if len(postData['password']) < 4:
            error_msgs.append("Password is too short!")

        if not postData['password'] == postData['confirm']:
            error_msgs.append("Passwords do not match!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(
        	name=postData['name'],
        	username=postData['username'],
        	password=hashed)
            return {'theuser':user.name, 'username':user.username, 'userid':user.id}

class User(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()


class TripManager(models.Manager):
	def add_trip_model(self, postData, userid):
		error_msgs = []
		
		if len(postData['destination']) < 2:
			error_msgs.append("no such destination!")

		if len(postData['description']) < 6:
			error_msgs.append("enter description!")
			print 'before error'

		start = postData['start'] 
		end = postData['end']
		print postData

		if not start:
			error_msgs.append("must start enter date.")

		if not end:
			error_msgs.append("must enter end date.")
		if error_msgs:
			return {'errors':error_msgs}
		start = postData['start'] 
		end = postData['end']
		# print start, 'hello'
		# start = datetime.strptime(start,'%Y-%m-%d').strftime('%Y/%m/%d')
		# end = datetime.strptime(end,'%Y-%m-%d').strftime('%Y/%m/%d')

		if start > end:
			error_msgs.append("start must be before end")

		if datetime.strptime(start,'%Y-%m-%d') < datetime.today():
			error_msgs.append("Start date must be later than today")

		print error_msgs
		if error_msgs:
			return {'errors':error_msgs}
		else:
			print 'im working'
			user = User.objects.get(id=userid)
			trip = Trip.objects.create(
			destination=postData['destination'],
			description=postData['description'],
			start=postData['start'],
			end=postData['end'],
			user=user)
			return {'trip_id': trip.id}

	


class Trip(models.Model):
	join = models.ManyToManyField(User, related_name="jointravels")
	destination = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	start = models.DateField(auto_now=False, auto_now_add=False)
	end = models.DateField(auto_now=False, auto_now_add=False)
	user = models.ForeignKey(User, related_name="trips")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = TripManager()

