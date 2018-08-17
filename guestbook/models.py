from django.db import models

# Create your models here.

class Image(models.Model):
    filename = models.CharField(max_length=30)
    img_title = models.CharField(max_length=30, default='SOME_STRING')
    img_desc = models.CharField(max_length=100, null=True)
    img_tags = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=200, default='')