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
    return render(request, 'profile_app/profile.html', {'trainer': User.objects.get(id=request.session['user_id'])})


def remove(request, trainer_ID):
    response = 'placeholder for removal of pokemon from team'
    return HttpResponse(response)


def edit(request, trainer_ID):
    return render(request, 'profile_app/edit_profile.html')
