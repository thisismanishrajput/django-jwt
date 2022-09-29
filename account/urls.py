
from django.contrib import admin
from django.urls import path
from account.views import SendPasswordResetEmailView, UserChangePassword, UserLoginView, UserPasswordResetView, UserProfileView, UserRegistrationView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('getProfile/',UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserChangePassword.as_view(),name='user change password'),
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name='user change password'),

    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name = 'reset-password')
]
