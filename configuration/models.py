# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Configuration(models.Model):
    """
    Description: Configuration Model
    """
    name = models.CharField(max_length=255, default='Config 1', unique=True)
    # header
    on_test = models.BooleanField(default=True)
    search_on = models.BooleanField(default=True)
    breaking_news_on = models.BooleanField(default=True)
    headline_on = models.BooleanField(default=True)
    slider_on = models.BooleanField(default=True)
    photo_news_on = models.BooleanField(default=True)

    # tab
    social_tab_on = models.BooleanField(default=True)
    latest_news_tabs_on = models.BooleanField(default=True)
    most_readable_news_tabs_on = models.BooleanField(default=True)
    todays_speech_tab_on = models.BooleanField(default=True)
    weather_on = models.BooleanField(default=True)
    live_score_board_tab_on = models.BooleanField(default=True)

    # adspace config
    adspace1_on = models.BooleanField(default=True)
    adspace2_on = models.BooleanField(default=True)
    adspace3_on = models.BooleanField(default=True)
    adspace4_on = models.BooleanField(default=True)
    adspace5_on = models.BooleanField(default=True)
    adspace6_on = models.BooleanField(default=True)
    adspace7_on = models.BooleanField(default=True)
    adspace8_on = models.BooleanField(default=True)
    adspace9_on = models.BooleanField(default=True)
    adspace10_on = models.BooleanField(default=True)
    adspace11_on = models.BooleanField(default=True)
    adspace12_on = models.BooleanField(default=True)
    adspace13_on = models.BooleanField(default=True)
    adspace14_on = models.BooleanField(default=True)
    adspace15_on = models.BooleanField(default=True)
    adspace16_on = models.BooleanField(default=True)
    adspace17_on = models.BooleanField(default=True)
    adspace18_on = models.BooleanField(default=True)

    # cache
    cache_on = models.BooleanField(default=True)

    # news type limit
    news_type_3_link_limit = models.IntegerField(default=5)
    news_type_4_link_limit = models.IntegerField(default=5)
    headline_limit = models.IntegerField(default=5)
    breaking_news_limit = models.IntegerField(default=3)
    latest_news_limit = models.IntegerField(default=10)
    most_readable_news_limit = models.IntegerField(default=10)

    # length
    default_words_count = models.IntegerField(default=38)
    latest_news_words_count = models.IntegerField(default=38)
    popular_news_words_count = models.IntegerField(default=40)
    most_readable_news_word_count = models.IntegerField(default=40)

    position_123_words_count = models.IntegerField(default=38)
    position_456_words_count = models.IntegerField(default=38)
    category_news_words_count = models.IntegerField(default=38)

    cache_timeout_hour = models.IntegerField(default=1)

    upload_image_width = models.IntegerField(default=600)
    upload_image_height = models.IntegerField(default=250)

    # default image
    sorry_nothing_found_text = models.CharField(max_length=255, default='দুঃখিত, কোন ফলাফল পাওয়া যায়নি')

    # footer

    chief_editor_name = models.CharField(max_length=255, verbose_name='প্রধান সম্পাদক', default='আলী হাসান')
    ceo_name = models.CharField(max_length=255, verbose_name='প্রধান নির্বাহী কর্মকর্তা', default='এস.এম.শামীম সুলতান')
    me_name = models.CharField(max_length=255, verbose_name='ব্যবস্থাপনা সম্পাদক', default='ফজলে রাব্বী')
    bureau_chief_name = models.CharField(max_length=255, verbose_name='ব্যবস্থাপনা সম্পাদক', default='আল মাসুম')

    # office address
    office_address = models.CharField(max_length=255, verbose_name='বার্তা ও বাণিজ্যিক কার্যালয়ঃ',
                                      default='স্যুট- ৫/ই, এ এইচ টাওয়ার (৫ম তলা), রোড-২, সেক্টর-৩, উত্তরা, ঢাকা-১২৩০')
    phones = models.CharField(max_length=255, verbose_name='ফোন', default='+৮৮ ০১৬৭৯-৮৮৬-৬৬৮')
    email = models.CharField(max_length=255, verbose_name='ই-মেইল', default='admin@bdtouchnews.tk, news@bdtouchnews.tk')

    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "News Configuration"
        verbose_name_plural = "News Configuration"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
