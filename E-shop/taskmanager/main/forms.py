from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from .models import  Resume


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Цена товара'
            }),
    }

from django import forms


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['email', 'name', 'file']
