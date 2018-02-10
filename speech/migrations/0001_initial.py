# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-10 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('by_whom', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Person Speech',
                'verbose_name_plural': 'Person Speech',
            },
        ),
    ]
