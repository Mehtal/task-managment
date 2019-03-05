from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import DateInput, DateTimeInput
from .models import Task, Project, Area


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

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("request")
    #     super(CreateAreaForm, self).__init__(*args, **kwargs)
    #     self.fields["project"].queryset = Area.objects.filter(project__id=self.request.GET.get("id"))
    #     print("form print ==============================")


# class BookSubmitForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop("request")
#         super(BookSubmitForm, self).__init__(*args, **kwargs)
#         self.fields["book"].queryset = Book.objects.filter(owner=self.request.user)
#         self.fields["whatever"].queryset = WhateverModel.objects.filter(user=self.request.user)
