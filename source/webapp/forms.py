from django import forms
from django.forms import widgets

from .models import TypeModel, StatusModel


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True, label='Summary')
    description = forms.CharField(max_length=2000, required=True, label='description', widget=widgets.Textarea)
    type = forms.ModelChoiceField(queryset=TypeModel.objects.all())
    status = forms.ModelChoiceField(queryset=StatusModel.objects.all())