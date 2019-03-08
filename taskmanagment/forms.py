from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import DateInput, DateTimeInput
from .models import Task, Project, Area, Personel, Observation


class CreateTaskForm(ModelForm):
    debut = forms.DateField(widget=DateTimeInput())
    fin = forms.DateField(widget=DateInput())
    # area = forms.ModelChoiceField(queryset=Area.objects.none())

    class Meta:
        model = Task
        fields = ['area', 'name', 'debut', 'fin', ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     project_id = request.GET.get("id")
    #     self.fields['area'].queryset = Area.objects.filter(id=project_id)


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', ]


class CreateAreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'project']


class CreatePersonelForm(ModelForm):
    class Meta:
        model = Personel
        fields = ["name", "task"]


class CreateObservationForm(ModelForm):
    class Meta:
        model = Observation
        fields = ["name", "task"]
