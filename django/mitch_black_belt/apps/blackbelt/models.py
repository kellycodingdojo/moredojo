from __future__ import unicode_literals
import re, bcrypt
from django.db import models
from datetime import datetime
# Create your models here.
class UserManager(models.Manager):
    def login(self, postData):
        error_msgs = []
        password = bcrypt.hashpw(postData['pass'].encode(), bcrypt.gensalt())

        try:
            user = User.objects.get(email=postData['email'])
        except:
            error_msgs.append("Invalid user!")
            return {'errors':error_msgs}

        if not bcrypt.hashpw(postData['pass'].encode(), user.password.encode()) == user.password.encode():
            error_msgs.append("Wrong Password!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            return {'theuser':user.name, 'user_name':user.user_name, 'userid':user.id}

    def register(self, postData):
        error_msgs = []
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        try:
            if User.objects.get(email=postData['email']):
                error_msgs.append("Email already in use!")
        except:
            pass

        if len(postData['name']) < 4:
            error_msgs.append("Name is too short!")

        if len(postData['user_name']) < 4:
            error_msgs.append("Username is too short!")

        if not email_regex.match(postData['email']):
            error_msgs.append("Invalid email!")

        if len(postData['pass']) < 8:
            error_msgs.append("Password is too short!")

        if not postData['pass'] == postData['pass_conf']:
            error_msgs.append("Passwords do not match!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            hashed = bcrypt.hashpw(postData['pass'].encode(), bcrypt.gensalt())
            user = User.objects.create(email=postData['email'], name=postData['name'], user_name=postData['user_name'], password=hashed)
            return {'theuser':user.name, 'user_name':user.user_name, 'userid':user.id}

class User(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()
    users = models.ManyToManyField(User, related_name='user_trips')
    created_by = models.ForeignKey(User, related_name='creator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()



class TripManager(models.Manager):
    def new_trip(self, postData):
        error_msgs = []

        if len(postData['dest']) < 1:
            error_msgs.append("Must have destination!")

        if len(postData['plan']) < 1:
            error_msgs.append("Must have description!")

        if len(postData['from_date']) < 1 or len(postData['to_date']) < 1:
            error_msgs.append("Dates cannot be left blank!")
        else:
            if datetime.strptime(postData['from_date'], '%Y-%m-%d') > datetime.strptime(postData['to_date'], '%Y-%m-%d'):
                error_msgs.append("End date must be later than start date!")
            if datetime.strptime(postData['from_date'], '%Y-%m-%d') < datetime.now():
                error_msgs.append("Start date must be in the future!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            user = User.objects.get(id=postData['userid'])
            trip = Trip.objects.create(destination=postData['dest'], start_date=postData['from_date'], end_date=postData['to_date'], plan=postData['plan'], created_by=user)
            trip.users.add(user)
            return {'noerrors': ''}


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()
    users = models.ManyToManyField(User, related_name='user_trips')
    created_by = models.ForeignKey(User, related_name='creator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
