from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, FormView

from .models import Issue
from .forms import IssueForm

# Create your views here.

class IndexView(TemplateView):
    def get(self, request, **kwargs):
        issues = Issue.objects.all()
        return render(request, 'index.html', {'issues': issues})

class IssueDetailView(TemplateView):
    template_name = 'issue_view.html'
    
    def get_context_data(self, **kwargs):
        kwargs['issue'] = get_object_or_404(Issue, pk=kwargs.get("pk"))
        return super().get_context_data(**kwargs)

class IssueCreateView(FormView):
    template_name = 'create.html'
    form_class = IssueForm

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse('issue_view', kwargs={'pk': self.issue.pk})

    
class IssueUpdateView(FormView):
    template_name = 'update.html'
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

class IssueDeleteView(FormView):
    template_name = 'delete.html'
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
        self.issue = form.delete()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Issue, pk=pk)