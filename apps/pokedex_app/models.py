# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import *
# Create your models here.

# import pokebase as pb


class Pokemon(models.Model):
    pk_ID = models.IntegerField()
    name = models.CharField(max_length=255)
    pk_type = models.CharField(max_length=255)
    pk_heigth = models.CharField(max_length=50)
    pk_weigth = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return 'id: '+unicode(self.id)+', name: '+self.name+', trainername: '+self.trainername
