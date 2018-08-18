from django.db import models
from django.utils.timezone import now
# class Image(models.Model):
#     photo     = models.ImageField(blank=True, null=True)
#     img_title = models.CharField(max_length=30, default='')
#     img_desc = models.CharField(max_length=100, default='', null=True)
#     img_tags = models.CharField(max_length=100, default='', null=True)
#     location = models.CharField(max_length=200, default='')

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

PHOTO_TYPE = (
    ('portrait','PORTRAIT'),
    ('landscape', 'LANDSCAPE'),
    ('candid','CANDID'),
    ('story','STORY'),
    ('wild','WILDLIFE'),
    ('selfie', 'SELFIE'),
)

class Image(models.Model):
    title = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    document     = models.ImageField(upload_to='images/', null=True)
    photo_type = models.CharField(max_length=10, choices=PHOTO_TYPE, default='portrait')
    uploaded_at = models.DateTimeField(default=now, blank=True)