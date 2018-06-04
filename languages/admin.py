# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Language, Paradigm, Programmer

# Register your models here.
admin.site.register(Language)
admin.site.register(Paradigm)
admin.site.register(Programmer)
