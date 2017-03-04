from __future__ import unicode_literals
import re, bcrypt
from django.db import models

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
            return {'theuser':user.name, 'alias':user.alias, 'userid':user.id}

    def register(self, postData):
        error_msgs = []
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        try:
            if User.objects.get(email=postData['email']):
                error_msgs.append("Email already in use!")
        except:
            pass

        date = postData['date']
        if not date:
			error_msgs.append("must  enter date.")

        if len(postData['name']) < 4:
            error_msgs.append("Name is too short!")

        if len(postData['alias']) < 4:
            error_msgs.append("Alias is too short!")

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
            user = User.objects.create(email=postData['email'], name=postData['name'], alias=postData['alias'], date=postData['date'], password=hashed)
            return {'theuser':user.name, 'alias':user.alias, 'userid':user.id, 'date':user.date}

class User(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    date = models.DateField(auto_now=False, auto_now_add=False)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class FriendManager(models.Manager):
	def add_friend(self, userid):
		 # newfriend = Friend.objects.create(userid=userid)
		
		return #{'friend': newfriend.id}
		

class Friend(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	users = models.ForeignKey(User, related_name="user")
	friends = models.ForeignKey(User, related_name="friend", null=True)
	objects = FriendManager()
