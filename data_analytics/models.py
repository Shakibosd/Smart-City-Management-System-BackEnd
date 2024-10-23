from django.db import models
from django.utils import timezone

class AnalyticsData(models.Model):
    total_users = models.IntegerField()
    total_transactions = models.IntegerField()
    traffic_issues = models.IntegerField()
    date = timezone.localtime(timezone.now())
