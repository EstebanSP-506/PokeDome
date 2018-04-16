# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from ..login_registration.models import *
from .models import *
import pokebase as pokebase
# Create your views here.


def pokedex(request):
    pokemons = pokebase.APIResourceList('pokemon')
    pokemon_list = []
    for pk in pokemons:
        pokemon_list.append(pokebase.NamedAPIResource('pokemon', pk['name']))
    print pokemon_list
    # print poke.id
    # print poke.name
    return render(request, 'pokedex_app/pokedex.html', {'pokemons': pokemons, 'pokebase': pokebase})


def get_pokemon(request, poke_ID):
    response = 'placeholder for get pokemons process and render pokedex with the pokemon data as context'
    return HttpResponse(response)


def add2team(request, poke_ID):
    response = 'placeholder process (including validation if the trainer already have 6 pokemons)'
    return HttpResponse(response)
