# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Paradigm(models.Model):
    name=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Language(models.Model):

    name=models.CharField(max_length=50, primary_key=True)
    paradigm=models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
