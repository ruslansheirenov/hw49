from django.shortcuts import render
from django.views.generic import View, TemplateView

from .models import Issue

# Create your views here.

class IndexView(TemplateView):
    def get(self, request, **kwargs):
        issues = Issue.objects.all()
        return render(request, 'index.html', {'issues': issues})

