# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Horoscope(models.Model):
    """
    Description: Horoscope model
    """
    ts = models.DateField(auto_now=False, verbose_name='Date')
    mesh = models.TextField(verbose_name='মেষ')
    brisho = models.TextField(verbose_name='বৃষ')
    mithun = models.TextField(verbose_name=' মিথুন')
    korkot = models.TextField(verbose_name='কর্কট')
    shingho = models.TextField(verbose_name='সিংহ')
    konna = models.TextField(verbose_name='কন্যা')
    tula = models.TextField(verbose_name='তুলা')
    brishchik = models.TextField(verbose_name='বৃশ্চিক')
    dhanu = models.TextField(verbose_name='ধনু')
    mokor = models.TextField(verbose_name='মকর')
    kumvo = models.TextField(verbose_name='কুম্ভ')
    meen = models.TextField(verbose_name='মীন')

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Horoscope"
        verbose_name_plural = "Horoscope"

    def __unicode__(self):
        ts = str(self.ts)
        return ts

    def __str__(self):
        ts = str(self.ts)
        return ts