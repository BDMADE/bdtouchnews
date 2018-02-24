# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Configuration(models.Model):
    """
    Description: Configuration Model
    """
    name = models.CharField(max_length=255, default='Config 1', unique=True)
    ts = models.DateTimeField(auto_now=True, verbose_name='Created at')
    # header
    on_test = models.BooleanField(default=True)
    search = models.BooleanField(default=True)
    breaking_news = models.BooleanField(default=True)
    headline = models.BooleanField(default=True)
    # social tab
    social = models.BooleanField(default=True)
    # news tab
    tabs1 = models.BooleanField(default=True)
    tabs2 = models.BooleanField(default=True)
    tabs3 = models.BooleanField(default=True)
    # adspace config
    adspace1 = models.BooleanField(default=True)
    adspace2 = models.BooleanField(default=True)
    adspace3 = models.BooleanField(default=True)
    adspace4 = models.BooleanField(default=True)
    adspace5 = models.BooleanField(default=True)
    adspace6 = models.BooleanField(default=True)
    adspace7 = models.BooleanField(default=True)
    adspace8 = models.BooleanField(default=True)
    adspace9 = models.BooleanField(default=True)
    adspace10 = models.BooleanField(default=True)
    adspace11 = models.BooleanField(default=True)
    adspace12 = models.BooleanField(default=True)
    adspace13 = models.BooleanField(default=True)
    adspace14 = models.BooleanField(default=True)
    adspace15 = models.BooleanField(default=True)
    adspace16 = models.BooleanField(default=True)
    adspace17 = models.BooleanField(default=True)
    adspace18 = models.BooleanField(default=True)

    # cache
    cache_on = models.BooleanField(default=True)

    # news type limit
    news_type_3_limit = models.IntegerField(default=5)
    news_type_4_limit = models.IntegerField(default=5)
    headline_limit = models.IntegerField(default=5)
    breaking_news_limit = models.IntegerField(default=3)
    latest_news = models.IntegerField(default=10)
    most_readable_news = models.IntegerField(default=10)

    # length
    default_trailer_length = models.IntegerField(default=250)
    latest_news_trailer_length = models.IntegerField(default=500)
    popular_news_trailer_length = models.IntegerField(default=900)
    most_readable_news_trailer_length = models.IntegerField(default=500)
    news_type_3_trailer_length = models.IntegerField(default=500)
    position_123_trailer_length = models.IntegerField(default=600)
    position_456_trailer_length = models.IntegerField(default=400)
    category_trailer_length = models.IntegerField(default=750)
    excerpt_length = models.IntegerField(default=20)
    search_trailer_length = models.IntegerField(default=750)
    search_trailer_length_word = models.IntegerField(default=50)
    default_word_limiter = models.IntegerField(default=250)
    cache_timeout = models.IntegerField(default=1)
    upload_image_width = models.IntegerField(default=600)
    upload_image_height = models.IntegerField(default=250)

    # path
    news_image_upload_path = models.CharField(max_length=255, default='assets/uploads/news/')
    ad_image_upload_path = models.CharField(max_length=255, default='assets/uploads/ads/')
    slider_image_upload_path = models.CharField(max_length=255, default='assets/uploads/slider/')
    video_image_upload_path = models.CharField(max_length=255, default='assets/uploads/video/')
    # default image
    default_news_image = models.CharField(max_length=255, default='no-image.png')
    default_ad_image = models.CharField(max_length=255, default='call-for-ad.png')
    default_slider_image = models.CharField(max_length=255, default='assets/uploads/slider/default.jpg')
    default_video_image = models.CharField(max_length=255, default='assets/uploads/video/no-image.png')
    sorry_nothing_found = models.CharField(max_length=255, default='দুঃখিত, কোন ফলাফল পাওয়া যায়নি')

    class Meta:
        verbose_name = "News Configuration"
        verbose_name_plural = "News Configuration"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
