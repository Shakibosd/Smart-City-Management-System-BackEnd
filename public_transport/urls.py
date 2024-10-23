from django.urls import path
from .views import PublicTransportAPIView, UpdateLocationView, TransportListView

urlpatterns = [
    path('transport/', PublicTransportAPIView.as_view(), name='transport'),
    path('transport_filter/', TransportListView.as_view(), name='transport-filter'),
    path('transport/update_location/<str:bus_number>/', UpdateLocationView.as_view(), name='update-location')
]
