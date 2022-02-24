from django.contrib import admin
from django.urls import path


from webapp.views import (
    IndexView, 
    IssueDetailView, 
    IssueCreateView, 
    IssueUpdateView, 
    IssueDeleteView, 
    ProjectIndexView, ProjectDetailView, ProjectCreateView)


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_view'),
    path('issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='update'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='delete'),
    path('projects', ProjectIndexView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_view'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
]