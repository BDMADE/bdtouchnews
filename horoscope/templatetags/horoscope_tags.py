# -*- coding: utf-8 -*-

from django import template
from django.template.loader import render_to_string
from horoscope.models import *

register = template.Library()


@register.simple_tag
def horoscope():
    try:
        last_horoscope = Horoscope.objects.last()
    except Horoscope.DoesNotExist:
        return ''

    horoscope_template = "horoscope/horoscope.html"
    content = render_to_string(horoscope_template, {'horoscope': last_horoscope})
    return content
