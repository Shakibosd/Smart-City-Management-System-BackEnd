from django.db import models

class EmergencyService(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    times_dates = models.DateTimeField(auto_now_add=True)