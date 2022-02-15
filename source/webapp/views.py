from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, reverse 
from django.views.generic import View, TemplateView, FormView, ListView, DeleteView
from django.utils.http import urlencode

from .models import Issue
from .forms import IssueForm, IssueSearchForm

# Create your views here.

#Вывод всеъ задач

class IndexView(ListView):
    context_object_name = 'issues'
    model = Issue
    template_name = 'issue/index.html'
    ordering = ['-id']
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
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return IssueSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

#Детальный просмотр задачи

class IssueDetailView(TemplateView):
    template_name = 'issue/issue_view.html'
    
    def get_context_data(self, **kwargs):
        kwargs['issue'] = get_object_or_404(Issue, pk=kwargs.get("pk"))
        return super().get_context_data(**kwargs)

#Создание новой задачи

class IssueCreateView(FormView):
    template_name = 'issue/create.html'
    form_class = IssueForm

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.issue.pk})

#Редактирование задачи
    
class IssueUpdateView(FormView):
    template_name = 'issue/update.html'
    form_class = IssueForm

    def dispatch(self, request, *args, **kwargs):
        self.issue = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.issue
        return kwargs

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.issue.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Issue, pk=pk)

#Удаление задачи

class IssueDeleteView(DeleteView):
    template_name = 'issue/delete.html'
    model = Issue
    success_url = reverse_lazy('index')