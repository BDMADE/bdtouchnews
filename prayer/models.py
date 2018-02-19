# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Prayer(models.Model):
    """
    Description: Prayer model
    """
    ts = models.DateField(auto_now=False, verbose_name='Date')
    fajar = models.CharField(max_length=255, verbose_name='Fajar Time')
    zohar = models.CharField(max_length=255, verbose_name='Zohar Time')
    asar = models.CharField(max_length=255, verbose_name='Asar Time')
    magrib = models.CharField(max_length=255, verbose_name='Magrib Time')
    esha = models.CharField(max_length=255, verbose_name='Esha Time')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Prayer Time"
        verbose_name_plural = "Prayer Time"

    def __unicode__(self):
        ts = str(self.ts)
        return ts

    def __str__(self):
        ts = str(self.ts)
        return ts
