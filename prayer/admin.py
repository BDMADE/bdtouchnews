# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.utils.html import format_html

# Register your models here.
from .models import Prayer

# Customizing admin


class PrayerAdmin(admin.ModelAdmin):
    def edit(self, obj):
        return format_html('<a class="btn" href="/admin/prayer/prayer/{}/change/">Edit</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn" href="/admin/prayer/prayer/{}/delete/">Delete</a>', obj.id)

    list_display = ('ts', 'fajar', 'zohar', 'asar', 'magrib', 'esha', 'edit', 'delete')
    list_filter = ('ts', )
    date_hierarchy = 'ts'

# register prayer model with django model
admin.site.register(Prayer, PrayerAdmin)
