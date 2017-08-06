# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Kitten(models.Model):
    #django automatically assigns ID
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo_url = models.TextField()
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    food_portion = models.FloatField()
    

    #allows three values: None, True, False
    fluffy_boolean = models.NullBooleanField()

    #user_id is the foreign key representing owner; when owner deleted, this kitten will be deleted too
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    timestamp_last_edited = models.DateField(auto_now=True, auto_now_add=False)
    timestamp_created = models.DateField(auto_now=False, auto_now_add=True)

    #tells Django which field to use as display on the Django admin (analgous to console but on the browser)
    def __str__(self):
        return self.name


