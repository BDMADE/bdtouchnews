# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

# load models
from .models import Website
from advertisement.models import Advertisement
from news.models import Category, News


# Create your views here.
def category_news(name):
# Return last five category based news      
    return News.objects.filter(category__name=name).all().order_by('updated_at').reverse()[:5]

# views for each category page
def category_page(request, category_name):
    news = category_news(category_name)
    context = {'category_news': news}
    return render(request,'category_page.html', context)

# views for news details page
def news_details(request, news_id):
    news = News.objects.get(pk=news_id)
    category_name = News.objects.get(pk=news_id).category.last().name
    other_news = category_news(category_name)
    context = {'news': news, 'other_news': other_news}
    return render(request, 'news_details.html', context)

def type3_view(request, name):
    context = {'name': name,}
    return render(request, 'type3.html', context)

# views for home page
def home(request):
    website = Website.objects.last()
    # advertisements = Advertisement.objects.first()
    position_1_news = News.objects.filter(category__name='position_1').last()
    position_2_news = News.objects.filter(category__name='position_2').last()
    position_3_news = News.objects.filter(category__name='position_3').last()
    position_4_news = News.objects.filter(category__name='position_4').last()
    position_5_news = News.objects.filter(category__name='position_5').last()
    position_6_news = News.objects.filter(category__name='position_6').last()
    position_7_news = News.objects.filter(category__name='position_7').last()
    position_8_news = News.objects.filter(category__name='position_8').last()
    position_9_news = News.objects.filter(category__name='position_9').last()
    popular_news = News.objects.filter(category__name='popular_news').last()
    # category based news
    entertainment = category_news('entertainment')
    sports = category_news('sports')
    education = category_news('education')
    science = category_news('science')
    life_style = category_news('life_style')
    national = category_news('national')
    politics = category_news('politics')
    economics = category_news('economics')
    international = category_news('international')
    foreign_life = category_news('foreign_life')
    health = category_news('health')
    photo_news = category_news('photo_news')
    crime = category_news('crime')
    accident = category_news('accident')
    court = category_news('court')
    media = category_news('media')
    travel = category_news('travel')
    woman_and_child = category_news('woman_and_child')
    kitchen = category_news('kitchen')
    mysterious_earth = category_news('mysterious_earth')
    struggle_of_life = category_news('struggle_of_life')
    editorial = category_news('editorial')
    admission_result = category_news('admission_result')
    library = category_news('library')
    bdtouch_special = category_news('bdtouch_special')
    bdtouch_blog = category_news('bdtouch_blog')

    context = {'website': website,
               'position_1_news': position_1_news,
               'position_2_news': position_2_news,
               'position_3_news': position_3_news,
               'position_4_news': position_4_news,
               'position_5_news': position_5_news,
               'position_6_news': position_6_news,
               'position_7_news': position_7_news,
               'position_8_news': position_8_news,
               'position_9_news': position_9_news,
               'popular_news': popular_news,
               'entertainment': entertainment,
               'sports' : sports,
               'education': education,
               'science': science,
               'life_style': life_style,
               'national': national,
               'politics': politics,
               'economics': economics,
               'international': international,
               'foreign_life': foreign_life,
               'health' : health,
               'photo_news': photo_news,
               'crime': crime,
               'accident': accident,
               'court': court,
               'media': media,
               'travel': travel,
               'woman_and_child': woman_and_child,
               'kitchen': kitchen,
               'mysterious_earth': mysterious_earth,
               'struggle_of_life': struggle_of_life,
               'editorial': editorial,
               'admission_result': admission_result,
               'library': library,
               'bdtouch_special': bdtouch_special,
               'bdtouch_blog': bdtouch_blog,
               }

    return render(request, 'home_page.html', context)
