from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import DateInput, DateTimeInput
from .models import Task, Project, Area


class CreateTaskForm(ModelForm):
    debut = forms.DateField(widget=DateTimeInput())
    fin = forms.DateField(widget=DateInput())

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
