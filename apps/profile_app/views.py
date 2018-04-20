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
    members = Team.objects.get(
        id=request.session['selected_team']).members.all()
    print trainer.name+' printed every time profile route is accessed'
    print teams
    print members
    return render(request, 'profile_app/profile.html', {'trainer': trainer, 'teams': teams, 'members': members})


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
        Team.objects.valid_team_add(postData, trainer_ID)

    return redirect('/trainer/'+trainer_ID)
