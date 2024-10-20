from django.db import models
from django.utils import timezone

class IncidentReport(models.Model):
    incident_type = models.CharField(max_length=100) 
    description  = models.TextField()
    reported_by = models.CharField(max_length=300)
    report_date  = timezone.localtime(timezone.now())
    location = models.CharField(max_length=200)
    