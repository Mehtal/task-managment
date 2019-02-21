from django import forms
from django.forms import ModelForm
from .models import Task, Project, Area


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['area', 'name', 'debut', 'fin', ]


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', ]


class CreateAreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'project']
