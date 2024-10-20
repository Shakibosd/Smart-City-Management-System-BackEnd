from django.contrib import admin
from .models import PublicTransport
from django.utils import timezone

class PublicTransportAdmin(admin.ModelAdmin):
    list_display = ['id', 'route_name', 'bus_number', 'available_seats', 'next_arrival_time']

admin.site.register(PublicTransport, PublicTransportAdmin)

