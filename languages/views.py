# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Paradigm, Programmer
from .serializer import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

# Create your views here.


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class =  LanguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class =  ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
