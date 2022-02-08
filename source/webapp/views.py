from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView

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

class IssueCreateView(View):
    def create_view(request):
        if request.method == 'GET':
            form = IssueForm()
            return render(request, 'create.html', {"form": form})
        else:
            form = IssueForm(data=request.POST)
            if form.is_valid():
                summary = form.cleaned_data.get('summary')
                description = form.cleaned_data.get('description')
                status = request.POST.get('status')
                type = request.POST.get('type')
                new_issue = Issue.objects.create(summary=summary, description=description, status=status, type=type)
                return redirect("ussue_view", pk=new_issue.pk)
            return render(request, 'create.html', {"form": form})
    