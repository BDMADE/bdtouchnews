# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Company(models.Model):
    """
    Description: Company model
    """
    ts = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=255, blank=True)
    phone2 = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Company"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Adspace(models.Model):
    """
    Description: Adspace model
    """
    ts = models.DateTimeField(auto_now=True, editable=True)
    name = models.CharField(max_length=255, unique=True)
    subscription_fees = models.DecimalField(max_digits=15, decimal_places=4)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Adspace"
        verbose_name_plural = "Adspace"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    """
    Description: Ads model
    """
    ACTIVE = '1'
    INACTIVE = '0'
    ADSTATUS_CHOICES = ((ACTIVE, 'active'), (INACTIVE, 'inactive'))

    ts = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(max_length=255, blank=True, upload_to='images/ads/')
    image_click_url = models.CharField(max_length=255)
    notes = models.TextField()

    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    adspace = models.OneToOneField(Adspace, on_delete=models.CASCADE)

    status = models.CharField(choices=ADSTATUS_CHOICES, max_length=2, default=INACTIVE)

    class Meta:
        verbose_name = "Ads"
        verbose_name_plural = "Ads"

    def __unicode__(self):
        return self.notes

    def __str__(self):
        return self.notes
