from django.contrib import admin
from .models import MobileAppFeature

class MobileAppFeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'version', 'release_date']

admin.site.register(MobileAppFeature, MobileAppFeatureAdmin)
