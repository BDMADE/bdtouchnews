# -*- coding: utf-8 -*-

from django import template
from django.template.loader import render_to_string
from django.utils.html import format_html
from poll.models import *
register = template.Library()


@register.simple_tag
def percentage(poll, item):
    poll_vote_count = poll.get_vote_count()
    if poll_vote_count > 0:
        return float(item.get_vote_count()) / float(poll_vote_count) * 100
