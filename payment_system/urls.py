from django.urls import path
from .views import PaymentInitiateAPIView, PaymentSuccessAPIView

urlpatterns = [
    path('initiate/', PaymentInitiateAPIView.as_view(), name='initiate_payment'),
    path('success/', PaymentSuccessAPIView.as_view(), name='payment_success'),
]
