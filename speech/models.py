# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Speech(models.Model):
    """
    Description: Today's Speech
    """
    ts = models.DateTimeField(auto_now=True)
    content = models.TextField()
    by_whom = models.CharField(max_length=255)

    class Meta:
    	verbose_name = "Person Speech"
    	verbose_name_plural = "Person Speech"
	    
    
    def __unicode__(self):
    	return self.by_whom

    def __str__(self):
    	return self.by_whom