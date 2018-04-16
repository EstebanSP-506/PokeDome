# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from ..login_registration.models import *
from ..pokedex_app.models import *
# Create your views here.


def battleground(request):
    response = 'placeholder for battleground'
    return HttpResponse(response)
