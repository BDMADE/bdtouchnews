# -*- coding: utf-8 -*-

import bangla
import datetime
import hijricalendar
from django import template
from django.template.loader import render_to_string

from configuration.models import Configuration
from news.models import News

register = template.Library()


@register.simple_tag
def get_bangla_date():
    today = str(datetime.date.today())
    current_year = int(today[:4])
    current_month = int(today[5:7])
    current_date = int(today[8:10])

    # convert greg form to bangla form

    greg_year = bangla.convert_english_digit_to_bangla_digit(current_year)
    greg_month = bangla.convert_greg_month_name(current_month)
    greg_date = bangla.convert_english_digit_to_bangla_digit(current_date)

    # get bangla calender date

    bangla_date_dict = bangla.get_date()
    date = bangla_date_dict['date'].decode('utf-8')
    month = bangla_date_dict['month'].decode('utf-8')
    year = bangla_date_dict['year'].decode('utf-8')
    weekday = bangla_date_dict['weekday'].decode('utf-8')
    session = bangla_date_dict['season'].decode('utf-8') + 'কাল'.decode('utf-8')

    # get bangla hijri calender date

    hijri_date_dict = hijricalendar.get_date()
    hijri_date = hijri_date_dict['date']
    hijri_month_name = hijricalendar.get_month_name()
    hijri_year = hijri_date_dict['year']

    context = {'date': date,
               'month': month,
               'year': year,
               'session': session,
               'weekday': weekday,
               'greg_year': greg_year,
               'greg_month': greg_month,
               'greg_date': greg_date,
               'hijri_date': hijri_date,
               'hijri_month_name': hijri_month_name,
               'hijri_year': hijri_year,
               }

    bangla_date_template = "website/bangla_date.html"
    content = render_to_string(bangla_date_template, context)
    return content


# return configuration objects
def get_config():
    try:
        config = Configuration.objects.last()
    except Configuration.DoesNotExist:
        return ''

    return config


# return news query
def set_query(category_name, limit):
    try:
        query = News.objects.filter(category__name=category_name).all().order_by('created_at').reverse()[:limit]
    except News.DoesNotExist:
        return ''
    return query


@register.simple_tag
def get_headlines():
    # headline_on =
    headline_limit = int(get_config().headline_limit)
    headlines = set_query('headline', headline_limit)

    headline_template = 'website/headlines.html'
    context = {'headlines': headlines }
    return render_to_string(headline_template, context)


