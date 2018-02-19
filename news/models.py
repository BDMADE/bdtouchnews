# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Description: Category model
    """
    TYPE1 = 'T1'
    TYPE2 = 'T2'
    TYPE3 = 'T3'
    TYPE4 = 'T4'
    NONE = 'NO'
    NEWS_CATEGORY_CHOICES = ((TYPE1, 'Type 1'), (TYPE2, 'Type 2'), (TYPE3, 'Type 3'), (TYPE4, 'Type 4'), (NONE, 'None'))

    ts = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    bangla_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    type = models.CharField(choices= NEWS_CATEGORY_CHOICES, max_length=2, default=NONE)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __unicode__(self):
        return self.bangla_name

    def __str__(self):
        return self.bangla_name


class News(models.Model):
    """
    Description: News model
    """
    headline = models.CharField(max_length=255, unique=True)
    category = models.ManyToManyField(Category)
    image_file = models.ImageField(blank=True, max_length=255, upload_to='images/news/')
    content = models.TextField()
    reporter = models.CharField(max_length=255, blank=True, default='অনলাইন প্রতিবেদক')
    hits = models.IntegerField(default=0)
    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __unicode__(self):
        return self.headline

    def __str__(self):
        return self.headline
