from django.urls import path
from .views import DeshboardAPIView

urlpatterns = [
    path('deshboard/', DeshboardAPIView.as_view(), name='deshboard')
]
