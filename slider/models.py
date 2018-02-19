from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Slider(models.Model):
    """
    Description: Video news
    """
    ts = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(max_length=255, upload_to='images/slider')
    caption = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Slider Picture"
        verbose_name_plural = "Slider Pictures"

    def __unicode__(self):
        return self.caption

    def __str__(self):
        return self.caption
