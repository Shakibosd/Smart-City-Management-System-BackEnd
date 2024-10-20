from django.urls import path
from .views import PublicTransportAPIView

urlpatterns = [
    path('transport/', PublicTransportAPIView.as_view(), name='transport')
]
