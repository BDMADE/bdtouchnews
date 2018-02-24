# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Company, Adspace, Advertisement

admin.site.register(Company)
admin.site.register(Adspace)
admin.site.register(Advertisement)
