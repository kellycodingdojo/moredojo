from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email_val_manager(models.Manager):
	def validate_email(self, post_data):
		error_msgs = []
		if len(post_data['email']) < 6:
			error_msgs.append('email length is not long enough')	
		elif not EMAIL_REGEX.match(post_data['email']):
			error_msgs.append('email not valid')

		if Email_val.objects.filter(email = post_data['email']).exists():
			error_msgs.append('email already in database')

		if error_msgs:
			return {
			'errors':error_msgs
			}

		else:
			create_email = Email_val.objects.create(email=post_data['email'])
			print create_email.email
			return{
			'the_email': create_email
			}

class Email_val(models.Model):
	email = models.CharField(max_length=50,unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	objects = Email_val_manager()