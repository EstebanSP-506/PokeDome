# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import *
import pokebase as pb
# Create your models here.

# import pokebase as pb


class TypeManager(models.Manager):
    def add_types(self, list_of_types):
        print self.all()
        if len(self.all()) == 0:
            for pk_type in list_of_types:
                print pk_type[1]
                # added_type = self.create(name=pk_type[1])
                # print added_type


class PokeType(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TypeManager()

    def __repr__(self):
        return 'type: '+self.name


class PokeManager(models.Manager):
    def add_pokemon(self, list_to_add):
        print len(self.all())
        if self.all() != 0:
            for pokemon in list_to_add:
                print pokemon
                name = pokemon[1]
                api_url = pokemon[0]
                if len(self.filter(name=name)) != 0:
                    print 'pokemon already exist'
                    continue
                # this pulls the pokemon object from the pokebase
                pokeData = pb.pokemon(name)
                pk_id = pokeData.id
                pk_height = pokeData.height
                pk_weight = pokeData.weight
                types = pokeData.types  # Types is a list including all the types for the pokemon
                print types

                newPokemon = self.create(
                    pk_id=pk_id, name=name, api_url=api_url, pk_height=pk_height, pk_weight=pk_weight)
                for pk_type in types:
                    name = pk_type.type
                    type2add = PokeType.objects.get(name=name)
                    newPokemon.pk_type.add(type2add)
                print newPokemon.pk_type.all()


class Pokemon(models.Model):
    objects = PokeManager()
    pk_id = models.IntegerField()
    name = models.CharField(max_length=255, unique=True)
    pk_type = models.ManyToManyField(
        PokeType, related_name='pkmns', blank=True)
    health = models.IntegerField(default=100)
    attack = models.IntegerField(default=50)
    defense = models.IntegerField(default=50)
    pk_height = models.IntegerField()
    pk_weight = models.IntegerField()
    api_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return 'pokemon ID: '+unicode(self.pk_id)+', name: '+self.name
