# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.utils.html import format_html

# Register your models here.
from .models import Category, News


class CategoryAdmin(admin.ModelAdmin):
    def edit(self, obj):
        return format_html('<a class="btn" href="/admin/news/category/{}/change/">Edit</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn" href="/admin/news/category/{}/delete/">Delete</a>', obj.id)

    list_display = ('name', 'bangla_name', 'type', 'edit', 'delete')
    search_fields = ('name', 'bangla_name', 'type')
    list_filter = ('type', )
    ordering = ('name', 'bangla_name', 'type', )

class NewsAdmin(admin.ModelAdmin):
    def edit(self, obj):
        return format_html('<a class="btn" href="/admin/news/news/{}/change/">Edit</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn" href="/admin/news/news/{}/delete/">Delete</a>', obj.id)

    list_display = ('headline', 'reporter', 'hits', 'publication_time', 'edit', 'delete')
    search_fields = ('headline', 'reporter')
    filter_horizontal = ('category', )
    list_filter = ('publication_time', 'reporter', 'category', )
    date_hierarchy = 'publication_time'
    ordering = ('headline', 'reporter', 'hits', 'publication_time', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
