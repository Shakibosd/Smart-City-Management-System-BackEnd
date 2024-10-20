from django.db import models

class MobileAppFeature(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    version = models.CharField(max_length=20)
    release_date = models.DateTimeField(auto_now_add=True)
