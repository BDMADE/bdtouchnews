# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Poll, Item, Vote

# Register your models here.


class PollItemInline(admin.TabularInline):
    model = Item
    extra = 0
    max_num = 15


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'date', 'vote_count', 'is_published')
    inlines = [PollItemInline,]


class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'ip', 'created_at')
    list_filter = ('poll', 'created_at')

# registration in admin
admin.site.register(Vote, VoteAdmin)
admin.site.register(Poll, PollAdmin)