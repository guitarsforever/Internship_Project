from django import forms
from general.models import (
Task, TaskStats
)

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class Status_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = TaskStats
        fields = ('post',)

class Completion_Date_form(forms.ModelForm):
    CompleteDate = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = Task
        fields = ('CompleteDate',)

class LaunchDateForm(forms.Form):
    Launchdate = forms.DateField(widget=DateInput())

