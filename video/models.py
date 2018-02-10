from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Video(models.Model):
    """
    Description: Video news
    """
    ts = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(max_length=255, upload_to='images/video/')
    image_click_url = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Video News"
        verbose_name_plural = "Video news"

    def __unicode__(self):
        return self.image_click_url

    def __str__(self):
        return self.image_click_url
