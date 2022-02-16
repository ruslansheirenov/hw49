from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, reverse 
from django.views.generic import View, TemplateView, FormView, ListView, DeleteView
from django.utils.http import urlencode

from webapp.models import Project
from webapp.forms import ProjectForm, ProjectSearchForm

class ProjectIndexView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/project_index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return ProjectSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None