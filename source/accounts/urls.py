from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import login_view, logout_view, RegisterView


app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/create/', RegisterView.as_view(), name='register'),
]