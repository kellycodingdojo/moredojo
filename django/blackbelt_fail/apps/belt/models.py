from __future__ import unicode_literals
import bcrypt, re, datetime
from django.db import models



class UserManager(models.Manager):
    def login(self, postData):
        error_msgs = []
        password = bcrypt.hashpw(postData['pass'].encode(), bcrypt.gensalt())

        try:
            user = User.objects.get(username=postData['username'])
        except:
            error_msgs.append("Invalid user!")
            return {'errors':error_msgs}

        if not bcrypt.hashpw(postData['pass'].encode(), user.password.encode()) == user.password.encode():
            error_msgs.append("Wrong Password!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            return {'theuser':user.username, 'userid':user.id}

    def register(self, postData):
		error_msgs = []

		try:
			if User.objects.get(username=postData['username']):
				error_msgs.append("Username already in use!")
		except:
			pass

		if len(postData['name']) < 3:
			error_msgs.append("Name is too short!")

		if len(postData['username']) < 3:
			error_msgs.append("Username is too short!")	

		if len(postData['pass']) < 8:
			error_msgs.append("Password is too short!")

		if not postData['pass'] == postData['pass_conf']:
			error_msgs.append("Passwords do not match!")

		if error_msgs:
			return {'errors':error_msgs}
		else:
			hashed = bcrypt.hashpw(postData['pass'].encode(), bcrypt.gensalt())
			user = User.objects.create(username=postData['username'],name=postData['name'], password=hashed)
			return {'theuser':user.username, 'userid': user.id}

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class TravelManager(models.Manager):
    def add(self, postData):
        error_msgs = []
        if len(postData['destination']) < 1:
            error_msgs.append("No destination!")

        if len(postData['description']) < 1:
            error_msgs.append("Must add description!")

        if len(postData['start']) < 1:
            error_msgs.append("must enter trip start date") 

        if len(postData['end']) < 1:
            error_msgs.append("must enter trip end date") 

        if error_msgs:
            return {'errors':error_msgs}
        else:
			trip = Travels.objects.create(destination=postData['destination'], start=postData['start'], end=postData['end'], user=User.objects.get(id=postData['userid']))
			return {'trip_id':trip.id, 'trip_dest':trip.destination, 'start':trip.start, 'end':trip.end, 'trip_description':trip.description}



class Travels(models.Model):
    destination = models.CharField(max_length=45)
    start = models.CharField(max_length=45)
    end = models.CharField(max_length=45)
    description = models.CharField(max_length=450)
    user = models.ForeignKey(User, related_name="travels")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()