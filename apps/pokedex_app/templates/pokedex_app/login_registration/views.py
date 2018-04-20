# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.


def index(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return redirect('/main')


def main(request):
    return render(request, 'login_registration/index.html')


def register(request):
    if request.method == 'POST':
        postData = request.POST
        validation = User.objects.valid_registration(postData)
        print 'register route'
        if not validation[0]:
            print validation[0]
            print validation[1]
            for error in validation[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            print validation[0]
            print validation[1]
            request.session['user_id'] = validation[1].id
            request.session.modified = True
            return redirect('/')
    return redirect('/main')


def login(request):
    if request.method == 'POST':
        postData = request.POST
        validation = User.objects.valid_login(postData)
        if not validation[0]:
            messages.add_message(request, messages.INFO, validation[1])
        else:
            request.session['user_id'] = validation[1].id
            request.session.modified = True
            return redirect('/')
    return redirect('/main')


def logout(request):
    request.session.clear()
    return redirect('/main')
