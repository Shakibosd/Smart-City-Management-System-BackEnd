from rest_framework import serializers
from .models import MobileAppFeature
from django.utils import timezone

class MobileAppFeatureSerializer(serializers.ModelSerializer):
    release_date = serializers.SerializerMethodField()
    
    class Meta:
        model = MobileAppFeature
        fields = ['id', 'name', 'description', 'version', 'release_date']
        
    def get_release_date(self, obj):
        local_time = timezone.localdate(obj.release_date)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")
            