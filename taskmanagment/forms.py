from django import forms
from django.forms import ModelForm
from .models import Task


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['area', 'name', 'debut', 'fin', ]


class CreateProjectForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', ]
