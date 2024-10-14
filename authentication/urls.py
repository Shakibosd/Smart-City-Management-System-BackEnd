from django.urls import path
from .views import RegisterAPIView, user_activate, LoginAPIView, LogoutAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('user_list/', UserListAPIView.as_view(), name='user_list'),
    path('user_detail/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', user_activate, name='active'),
]
