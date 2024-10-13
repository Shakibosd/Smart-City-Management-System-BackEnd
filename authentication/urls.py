from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, RegisterAPIView, activate, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('users_list/', UserListAPIView.as_view(), name='user-list'),
    path('users_detail/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', activate, name='active'),
]