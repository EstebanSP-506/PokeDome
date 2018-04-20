# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from ..login_registration.models import *
from .models import *
import pokebase as pb
import itertools
# Create your views here.


def pokedex(request):
    if 'poke_id' not in request.session:
        request.session['poke_id'] = 1
    pokemons = Pokemon.objects.all()
    pokeData = Pokemon.objects.get(pk_id=request.session['poke_id'])
    pokeTypes = pokeData.pk_type.all()
    # pokemons2 = pb.APIResourceList('pokemon')
    # types = pb.APIResourceList('type')
    # print types
    # typeList = []
    # for pk_type in types:
    #     print pk_type['url']
    #     print pk_type['name']
    #     typeList.append((pk_type['url'], pk_type['name']))

    # pokeList = []

    # for pk in itertools.islice(pokemons2, 0, 151):
    #     print pk
    #     print pk['url']
    #     print pk['name']
    #     pokeList.append((pk['url'], pk['name']))

    # print pokeList
    # for pkm in pokeList:
    #     print pkm[0]
    #     print pkm[1]
    # PokeType.objects.add_types(typeList)
    # Pokemon.objects.add_pokemon(pokeList)
    context = {'pokemons': pokemons, 'pb': pb,
               'pokeData': pokeData, 'pokeTypes': pokeTypes}
    return render(request, 'pokedex_app/pokedex.html', context)


def get_pokemon(request, poke_ID):
    request.session['poke_id'] = poke_ID
    request.session.modified = True
    return redirect('/pokedex/')


def add2team(request, poke_ID):
    response = 'placeholder process (including validation if the trainer already have 6 pokemons)'
    return HttpResponse(response)


def pokedex_builder(request):
    pk_id = 500
    return render(request, 'pokedex_app/pokedex_builder.html', {'pokemon_ID': pk_id})
