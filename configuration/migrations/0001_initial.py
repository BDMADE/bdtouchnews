# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-10 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Config 1', max_length=255)),
                ('ts', models.DateTimeField(auto_now=True)),
                ('on_test', models.BooleanField(default=True)),
                ('search', models.BooleanField(default=True)),
                ('breaking_news', models.BooleanField(default=True)),
                ('headline', models.BooleanField(default=True)),
                ('social', models.BooleanField(default=True)),
                ('tabs1', models.BooleanField(default=True)),
                ('tabs2', models.BooleanField(default=True)),
                ('tabs3', models.BooleanField(default=True)),
                ('adspace1', models.BooleanField(default=True)),
                ('adspace2', models.BooleanField(default=True)),
                ('adspace3', models.BooleanField(default=True)),
                ('adspace4', models.BooleanField(default=True)),
                ('adspace5', models.BooleanField(default=True)),
                ('adspace6', models.BooleanField(default=True)),
                ('adspace7', models.BooleanField(default=True)),
                ('adspace8', models.BooleanField(default=True)),
                ('adspace9', models.BooleanField(default=True)),
                ('adspace10', models.BooleanField(default=True)),
                ('adspace11', models.BooleanField(default=True)),
                ('adspace12', models.BooleanField(default=True)),
                ('adspace13', models.BooleanField(default=True)),
                ('adspace14', models.BooleanField(default=True)),
                ('adspace15', models.BooleanField(default=True)),
                ('adspace16', models.BooleanField(default=True)),
                ('adspace17', models.BooleanField(default=True)),
                ('adspace18', models.BooleanField(default=True)),
                ('cache_on', models.BooleanField(default=True)),
                ('news_type_3_limit', models.IntegerField(default=5)),
                ('news_type_4_limit', models.IntegerField(default=5)),
                ('headline_limit', models.IntegerField(default=5)),
                ('breaking_news_limit', models.IntegerField(default=3)),
                ('latest_news', models.IntegerField(default=10)),
                ('most_readable_news', models.IntegerField(default=10)),
                ('default_trailer_length', models.IntegerField(default=250)),
                ('latest_news_trailer_length', models.IntegerField(default=500)),
                ('popular_news_trailer_length', models.IntegerField(default=900)),
                ('most_readable_news_trailer_length', models.IntegerField(default=500)),
                ('news_type_3_trailer_length', models.IntegerField(default=500)),
                ('position_123_trailer_length', models.IntegerField(default=600)),
                ('position_456_trailer_length', models.IntegerField(default=400)),
                ('category_trailer_length', models.IntegerField(default=750)),
                ('excerpt_length', models.IntegerField(default=20)),
                ('search_trailer_length', models.IntegerField(default=750)),
                ('search_trailer_length_word', models.IntegerField(default=50)),
                ('default_word_limiter', models.IntegerField(default=250)),
                ('cache_timeout', models.IntegerField(default=1)),
                ('upload_image_width', models.IntegerField(default=600)),
                ('upload_image_height', models.IntegerField(default=250)),
                ('news_image_upload_path', models.CharField(default='assets/uploads/news/', max_length=255)),
                ('ad_image_upload_path', models.CharField(default='assets/uploads/ads/', max_length=255)),
                ('slider_image_upload_path', models.CharField(default='assets/uploads/slider/', max_length=255)),
                ('video_image_upload_path', models.CharField(default='assets/uploads/video/', max_length=255)),
                ('default_news_image', models.CharField(default='no-image.png', max_length=255)),
                ('default_ad_image', models.CharField(default='call-for-ad.png', max_length=255)),
                ('default_slider_image', models.CharField(default='assets/uploads/slider/default.jpg', max_length=255)),
                ('default_video_image', models.CharField(default='assets/uploads/video/no-image.png', max_length=255)),
                ('sorry_nothing_found', models.CharField(default='\u09a6\u09c1\u0983\u0996\u09bf\u09a4, \u0995\u09cb\u09a8 \u09ab\u09b2\u09be\u09ab\u09b2 \u09aa\u09be\u0993\u09df\u09be \u09af\u09be\u09df\u09a8\u09bf', max_length=255)),
            ],
            options={
                'verbose_name': 'News Configuration',
                'verbose_name_plural': 'News Configuration',
            },
        ),
    ]
