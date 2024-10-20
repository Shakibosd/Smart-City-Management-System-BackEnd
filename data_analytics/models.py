from django.db import models

class AnalyticsData(models.Model):
    total_users = models.IntegerField()
    total_transactions = models.IntegerField()
    traffic_issues = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
