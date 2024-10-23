from django.db import models
from django.utils import timezone

class MobileAppFeature(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    version = models.CharField(max_length=20)
    release_date = timezone.localtime(timezone.now())
