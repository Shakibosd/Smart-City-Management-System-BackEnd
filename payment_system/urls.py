from django.urls import path
from .views import PaymentAPIView

urlpatterns = [
    path('payment/', PaymentAPIView.as_view(), name='payment')
]
