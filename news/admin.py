# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Category, News


class NewsAdmin(admin.ModelAdmin):
    filter_horizontal = ('category', )

admin.site.register(Category)
admin.site.register(News, NewsAdmin)
