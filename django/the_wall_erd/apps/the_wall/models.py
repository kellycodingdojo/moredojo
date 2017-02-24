from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
class Message(models.Model):
	message = models.TextField(max_length=1000)
	# Notice the association made with ForeignKey for a one-to-many relationship
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
	message_id = models.ForeignKey(Message)
	user_id = models.ForeignKey(User)
	comment = models.TextField(max_length=45)
	created_at = models.DateTimeField(auto_now_add =True)
	updated_at = models.DateTimeField(auto_now = True)   
