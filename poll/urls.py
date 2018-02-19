from django.conf.urls import url
from .views import vote, poll_view, result

urlpatterns = [
    url(r'^votes/(?P<poll_id>[0-9]+)/$', vote, name='vote'),
    url(r'^polls/(?P<poll_id>[0-9]+)/', poll_view, name='poll_view'),
    url(r'^result/(?P<poll_id>[0-9]+)/$', result, name='result'),
]
