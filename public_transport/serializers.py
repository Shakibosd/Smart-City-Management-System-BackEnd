from rest_framework import serializers
from .models import PublicTransport
from django.utils import timezone

class PublicTransportSerializer(serializers.ModelSerializer):
    next_arrival_time = serializers.SerializerMethodField()


    class Meta:
        model = PublicTransport
        fields = ['id', 'route_name', 'bus_number', 'available_seats', 'next_arrival_time', 'current_latitude', 'current_longitude', 'last_update', 'schedules']
        
    def get_next_arrival_time(self, obj):
        local_time = timezone.localtime(obj.next_arrival_time)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")  
