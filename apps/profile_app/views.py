# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.


def get_trainer(request):
    response = 'placeholder for profile'
    return HttpResponse(response)


def profile(request, trainer_ID):
    response = 'placeholder for profile'
    return HttpResponse(response)


def remove(request, trainer_ID):
    response = 'placeholder for removal of pokemon from team'
    return HttpResponse(response)
