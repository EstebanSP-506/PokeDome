# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


class UserManager(models.Manager):
    def valid_registration(self, postData):
        name = postData['name']
        trainername = postData['trainername']
        password = postData['password']
        c_password = postData['c_password']
        errors = []
        if len(name) == 0:
            errors.append('Please enter a name')
        elif len(name) < 5:
            errors.append('Name must be at least 5 characters')
        if len(trainername) == 0:
            errors.append('Please enter a trainername')
        elif len(trainername) < 5:
            errors.append('Trainername must be at least 5 characters')
        if len(password) == 0:
            errors.append('Please enter a password')
        elif len(password) < 8:
            errors.append('Password must be at least 8 characters')
        if password != c_password:
            errors.append('Password Confirmation must match Password')
        if len(errors) != 0:
            return (False, errors)
        else:
            is_user = User.objects.filter(trainername=trainername)
            if len(is_user) != 0:
                errors.append('Please try a different TrainerName')
                return (False, errors)
            else:
                enc_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                self.create(
                    name=name, trainername=trainername, password=enc_pass)
                return (True, self.last())
        print trainername
        pass

    def valid_login(self, postData):
        trainername = postData['trainername']
        password = postData['password']
        user = self.filter(trainername=trainername)
        if len(user) == 0:
            return(False, "Invalid TrainerName/Password Combination")
        else:
            user_pass = user[0].password
            if bcrypt.checkpw(password.encode(), user_pass.encode()):
                return (True, user[0])
        return(False, "Invalid TrainerName/Password Combination")


class User(models.Model):
    name = models.CharField(max_length=255)
    trainername = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    preferred_team = models.IntegerField(blank=True, null=True)
    battles_won = models.IntegerField(default=0)
    battles_lost = models.IntegerField(default=0)
    picture = models.ImageField(
        upload_to='user_picture/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return 'id: '+unicode(self.id)+', name: '+self.name+', trainername: '+self.trainername
