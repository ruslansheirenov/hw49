from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import login_view, logout_view, RegisterView, UserDetailView, UserListView


app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/create/', RegisterView.as_view(), name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('accounts/list/', UserListView.as_view(), name='user_list'),
]