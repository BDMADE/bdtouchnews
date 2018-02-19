from django.conf.urls import url
from .views import home, news_details, category_page

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^details/(?P<news_id>[0-9]+)/', news_details, name='news_details'),
    url(r'^category/(?P<category_name>[a-z_]+)/', category_page, name='category_page'),

]