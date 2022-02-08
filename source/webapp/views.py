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
    
class IssueUpdateView(View):
    def update_view(request):
        issue = get_object_or_404(Issue, pk=kwargs.get("pk"))
        if request.method == 'GET':
            form = IssueForm(initial={
                'summary': issue.summary,
                'description': issue.description,
                'status': issue.status, 
                'type': issue.type
            })
            return render(request, 'update.html', {"issue": issue, "form": form})
        else:
            form = IssueForm(data=request.POST)
            if form.is_valid():
                issue.product_name = request.POST.get('summary')
                issue.description = request.POST.get('description')
                issue.category = request.POST.get('status')
                issue.remainder = request.POST.get('type')
                issue.save()
                return redirect("issue_view", pk)
            return render(request, 'update.html', {"issue": issue, "form": form})

class IssueDeleteView(View):
    def delete_view(request):
        issue = get_object_or_404(Issue, pk=kwargs.get("pk"))
        if request.method == 'GET':
            return render(request, "delete.html", {"issue": issue})
        else:
            issue.delete()
            return redirect("index")