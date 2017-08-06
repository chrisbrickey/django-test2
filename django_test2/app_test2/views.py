# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
# from django.core import serializers
from .models import Kitten



def index(request):
    all_kittens = Kitten.objects.all()

    # kitten_list = serializers.serialize('json', all_kittens)

    kitten_dict = {}

    for kitten in all_kittens:
        kitten_dict = {'id' : kitten.id, 'name' : kitten.name, 'description' : kitten.description }

    return JsonResponse({'kittens': kitten_dict})



def detail(request, kitten_id):
    all_kittens = Kitten.objects.all()
    return JsonResponse({ 'kitten_id' : all_kittens.filter(kitten_id) })


