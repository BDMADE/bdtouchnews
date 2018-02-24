# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.utils.html import format_html

# Register your models here.
from .models import Configuration


class ConfigurationAdmin(admin.ModelAdmin):
    def edit(self, obj):
        return format_html('<a class="changelink" href="/admin/configuration/configuration/{}/change/"></a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="deletelink" href="/admin/configuration/configuration/{}/delete/"></a>', obj.id)

    list_display = ('name', 'ts', 'edit', 'delete')

admin.site.register(Configuration, ConfigurationAdmin)
