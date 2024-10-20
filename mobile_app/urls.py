from django.urls import path
from .views import MobileAppFeatureView

urlpatterns = [
    path('features/', MobileAppFeatureView.as_view(), name='mobile-features'),
]
