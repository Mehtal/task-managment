from django.shortcuts import render, reverse
from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from taskmanagment.models import Project, Tool, Task, Area, Personel, Observation
from .forms import CreateTaskForm, CreateProjectForm, CreateAreaForm, CreatePersonelForm, CreateObservationForm
from django.urls import reverse_lazy
# Create your views here.


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ["name", "description"]
    template_name = "add-project.html"


class ProjectCreateView(CreateView):
    model = Project
    template_name = "add-project.html"
    fields = ['name', ]


class ProjectListView(ListView):
    queryset = Project.objects.all().order_by("name")
    template_name = 'project.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['create_form'] = CreateProjectForm()
        context['delete_form'] = CreateProjectForm()
        return context


class ProjectDetailView(DetailView):
    template_name = 'project-detail.html'

    def get_queryset(self):
        return Project.objects.all().prefetch_related('areas', 'areas__tasks', 'areas__project')

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        area_form_data = {"project": self.object.id}
        task_form_data = {"area": self.object.areas.first()}
        print(self.object.areas.all())
        context['area_form'] = CreateAreaForm(initial=area_form_data)
        context['task_form'] = CreateTaskForm(initial=task_form_data)
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("task:project-list")
    template_name = "delete-project.html"


# AREA CRUD
class AreaCreateView(CreateView):
    form_class = CreateAreaForm
    template_name = "add-area.html"
    success_url = "/"


# TASK CRUD

class TaskCreateView(CreateView):
    form_class = CreateTaskForm
    template_name = 'add-task.html'


class TaskDetailView(DetailView):
    template_name = 'task-detail.html'

    def get_queryset(self):
        queryset = Task.objects.all().select_related("area", "area__project")
        return queryset

    def get_sum(self, my_sum=0):
        for tool in self.object.tools.all():
            my_sum += tool.get_total()
        return my_sum

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        form_data1 = {"task": self.object.id}
        context['personel_form'] = CreatePersonelForm(initial=form_data1)
        context['observation_form'] = CreateObservationForm(initial=form_data1)
        return context


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["name", "debut", "fin", "start", "complete", "area"]
    template_name = 'add-task.html'

# personel Crud


class PersonelCreateView(CreateView):
    form_class = CreatePersonelForm
    template_name = "add-personel.html"


class PersonelDeleteView(DeleteView):
    model = Personel
    template_name = "delete-project.html"


# Observation Crud

class ObservationCreateView(CreateView):
    form_class = CreateObservationForm
    template_name = "add-observation.html"


class ObservationDeleteView(DeleteView):
    model = Observation
    template_name = "delete-project.html"
