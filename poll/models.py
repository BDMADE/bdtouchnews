# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Poll(models.Model):
    date = models.DateField()
    question = models.CharField(max_length=255, unique=True)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.question


class Item(models.Model):
    value = models.CharField(max_length=255, unique=True)
    position = models.SmallIntegerField(default=1, unique=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __unicode__(self):
        return self.value

    def __str__(self):
        return self.value


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name='voted item', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(verbose_name='ip address')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __unicode__(self):
        return self.ip

    def __str__(self):
        return self.ip
