from django import forms
from others.models import (
Task, TaskStat
)

class Status_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = TaskStat
        fields = ('post',)

class Completion_Date_form(forms.ModelForm):
    CompleteDate = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = Task
        fields = ('CompleteDate',)