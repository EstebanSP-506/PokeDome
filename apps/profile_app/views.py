# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from ..login_registration.models import *
from ..pokedex_app.models import *
from .models import *
# Create your views here.


def get_trainer(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return redirect('/trainer/'+str(request.session['user_id']))


def profile(request, trainer_ID):
    trainer = User.objects.get(id=trainer_ID)
    teams = trainer.owns_teams.all()
    attack = 0
    defense = 0
    if 'selected_team' not in request.session:
        try:
            request.session['selected_team'] = trainer.owns_teams.last().id
        except:
            len(teams) == 0

    if len(teams) == 0:
        messages.add_message(
            request, messages.ERROR, 'please create a Team in order to Start your adventure')
        selected_team = []
        members = []
    else:
        print request.session['selected_team']
        print trainer.owns_teams.all()
        for team in trainer.owns_teams.all():
            if int(request.session['selected_team']) == int(team.id):
                print team.id
                selected_team = trainer.owns_teams.get(
                    id=request.session['selected_team'])
                members = selected_team.members.all()
                for pokemon in members:
                    attack += pokemon.attack
                    defense += pokemon.defense
                break
            else:
                selected_team = None
                members = None

    print trainer.name+' printed every time profile route is accessed'
    # print teams
    # print members
    return render(request, 'profile_app/profile.html', {'trainer': trainer, 'teams': teams, 'members': members, 'selected_team': selected_team, 'attack': attack, 'defense': defense})


def remove(request, trainer_ID):
    response = 'placeholder for removal of pokemon from team'
    return HttpResponse(response)


def edit(request, trainer_ID):
    return render(request, 'profile_app/edit_profile.html')


def select_team(request, trainer_ID, team_ID):
    request.session['selected_team'] = team_ID
    request.session.modified = True
    trainer = User.objects.get(id=trainer_ID)
    trainer.preferred_team = team_ID
    trainer.save()
    return redirect('/trainer/'+trainer_ID)


def add_team(request, trainer_ID):
    if request.method == "POST":
        postData = request.POST
        print postData['team_name']
        validation = Team.objects.valid_team_add(postData, trainer_ID)
        if validation[0]:
            messages.add_message(
                request, messages.SUCCESS, 'Team Created Successfully')
        else:
            messages.add_message(
                request, messages.ERROR, validation[1])
    return redirect('/trainer/'+trainer_ID)
