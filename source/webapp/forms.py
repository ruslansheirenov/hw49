from django import forms

from .models import Issue


class IssueForm(forms.Form):
    class Meta:
        model = Issue
        exlude = []