from django import forms
from django.core.exceptions import ValidationError

from .models import Issue, Project


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = []
        widgets = {
            'type': forms.CheckboxSelectMultiple
        }

    def clean(self):
        cleaned_data = super().clean()
        summary = cleaned_data['summary']
        description = cleaned_data['description']
        if len(summary) < 5:
            self.add_error('summary', ValidationError(f'Значение должно быть более 5 символов. {summary} не подходит.'))
        if summary == content:
            raise ValidationError("Text of the issue should not duplicate it's title!")
        return cleaned_data

class IssueSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="search")

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = []

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data['title']
        description = cleaned_data['description']
        if len(title) < 5:
            self.add_error('summary', ValidationError(f'Значение должно быть более 5 символов. {title} не подходит.'))
        if title == content:
            raise ValidationError("Text of the issue should not duplicate it's title!")
        return cleaned_data

class ProjectSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="search")