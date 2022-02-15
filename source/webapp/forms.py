from django import forms

from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = []

class IssueSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="search")