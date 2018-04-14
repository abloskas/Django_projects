from __future__ import unicode_literals

from django.db import models

import md5
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First Name must be longer than 2 characters"   
        if len(postData['lname']) < 2:
            errors['lname'] = "Last Name must be longer than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = 'Email invalid'  
        # if not User.objects.filter(email=postData['email']) == []:
		# 	errors['iemail'] = 'You already have an account'    
        return errors    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
		return "<User object: {} {} {} {}".format(self.first_name, self.last_name, self.email, self.created_at)        