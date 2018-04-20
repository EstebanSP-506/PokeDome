# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here.


class UserManager(models.Manager):
    def valid_registration(self, postData):
        name = postData['name']
        username = postData['username']
        password = postData['password']
        c_password = postData['c_password']
        errors = []
        if len(name) == 0:
            errors.append('Please enter a name')
        elif len(name) < 3:
            errors.append('Name must be at least 3 characters')
        if len(username) == 0:
            errors.append('Please enter a username')
        elif len(username) < 3:
            errors.append('username must be at least 3 characters')
        if len(password) == 0:
            errors.append('Please enter a password')
        elif len(password) < 8:
            errors.append('Password must be at least 8 characters')
        if password != c_password:
            errors.append('Password Confirmation must match Password')
        if len(errors) != 0:
            return (False, errors)
        else:
            is_user = User.objects.filter(username=username)
            if len(is_user) != 0:
                errors.append('Please try a different Username')
                return (False, errors)
            else:
                enc_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                self.create(
                    name=name, username=username, password=enc_pass)
                return (True, self.last())
        print username
        pass

    def valid_login(self, postData):
        username = postData['username']
        password = postData['password']
        user = self.filter(username=username)
        if len(user) == 0:
            return(False, "Invalid Username/Password Combination")
        else:
            user_pass = user[0].password
            if bcrypt.checkpw(password.encode(), user_pass.encode()):
                return (True, user[0])
        return(False, "Invalid Username/Password Combination")


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return 'id: '+unicode(self.id)+', name: '+self.name+', username: '+self.username
