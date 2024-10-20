from django.db import models
from django.utils import timezone


class PublicTransport(models.Model):
    route_name = models.CharField(max_length=200)
    bus_number = models.CharField(max_length=30)
    available_seats = models.IntegerField()
    next_arrival_time = timezone.localtime(timezone.now())