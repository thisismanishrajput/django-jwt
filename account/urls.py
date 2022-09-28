
from django.contrib import admin
from django.urls import path
from account.views import UserLoginView, UserProfileView, UserRegistrationView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('getProfile/',UserProfileView.as_view(),name='profile'),
]
