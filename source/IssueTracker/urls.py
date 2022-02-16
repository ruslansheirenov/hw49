"""IssueTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import (
    IndexView, 
    IssueDetailView, 
    IssueCreateView, 
    IssueUpdateView, 
    IssueDeleteView, 
    ProjectIndexView, ProjectDetailView, ProjectCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_view'),
    path('issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='update'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='delete'),
    path('projects', ProjectIndexView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_view'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create')
]
