# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.utils.html import format_html

# Register your models here.
from .models import Horoscope


class HoroscopeAdmin(admin.ModelAdmin):
    def edit(self, obj):
        return format_html('<a class="changelink" href="/admin/prayer/prayer/{}/change/"></a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="deletelink" href="/admin/prayer/prayer/{}/delete/"></a>', obj.id)

    list_display = ('ts', 'edit', 'delete')


admin.site.register(Horoscope, HoroscopeAdmin)
