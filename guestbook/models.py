from django.db import models


class Image(models.Model):
    photo     = models.ImageField(blank=True, null=True)
    img_title = models.CharField(max_length=30, default='')
    img_desc = models.CharField(max_length=100, default='', null=True)
    img_tags = models.CharField(max_length=100, default='', null=True)
    location = models.CharField(max_length=200, default='')

class EXIF_data(models.Model):
    exposure_mode   = models.CharField(max_length=10, null=True)
    focal_length    = models.CharField(max_length=10, null=True)
    lens            = models.CharField(max_length=10, null=True)
    apparture       = models.CharField(max_length=10, null=True)
    metering_mode   = models.CharField(max_length=10, null=True)
    white_balance   = models.CharField(max_length=10, null=True)
    make            = models.CharField(max_length=10, null=True)
    model           = models.CharField(max_length=10, null=True)
    date_created    = models.DateTimeField(null=True)
    date_modified   = models.DateTimeField(null=True)
    resolution      = models.CharField(max_length=10, null=True)
