# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import *
from ..pokedex_app.models import *
# Create your models here.


class TeamManager(models.Manager):
    def valid_team_add(self, postData, trainer_ID):
        name = postData['team_name']
        if len(name) == 0:
            return(False, 'Please Enter a Team name')
        trainer = User.objects.get(id=trainer_ID)
        new_team = trainer.owns_teams.create(name=name)
        print trainer.trainername
        print 'team name: '+name
        return (True, new_team)

    def add_to_team(self, team_ID, trainer_ID, pokemon_ID):
        trainer = User.objects.get(id=trainer_ID)
        team = trainer.owns_teams.get(id=team_ID)
        pokemon = Pokemon.objects.get(pk_id=pokemon_ID)
        # add to team
        team.members.add(pokemon)
        return (True, 'successfully added to team')


class Team(models.Model):
    name = models.CharField(max_length=255, blank=True)
    members = models.ManyToManyField(
        Pokemon, related_name='used_in_teams', blank=True)
    trainer = models.ForeignKey(
        User, related_name='owns_teams', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TeamManager()
