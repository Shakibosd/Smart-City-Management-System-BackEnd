from django.contrib import admin
from .models import PublicTransport

class PublicTransportAdmin(admin.ModelAdmin):
    list_display = ['id', 'route_name', 'bus_number', 'available_seats', 'next_arrival_time', 'current_latitude', 'current_longitude', 'last_update']

admin.site.register(PublicTransport, PublicTransportAdmin)

