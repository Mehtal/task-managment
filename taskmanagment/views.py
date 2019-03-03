from django.shortcuts import render, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from taskmanagment.models import Project, Tool, Task, Area
from .forms import CreateTaskForm, CreateProjectForm, CreateAreaForm
from django.urls import reverse_lazy
# Create your views here.


# project CRUD
# def ProjectView(request):
#     project = Project.objects.all()
#     template = 'project.html'
#     return render(request, template, {'project': project})


# def dashboard(request):
#     return render(request, 'dashboard.html', {})


class ProjectCreateView(CreateView):
    model = Project
    template_name = "add-project.html"
    fields = ['name', ]


class ProjectListView(ListView):
    queryset = Project.objects.all()
    template_name = 'project.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['create_form'] = CreateProjectForm()
        context['delete_form'] = CreateProjectForm()
        return context


class ProjectDetailView(DetailView):
    #model = Project
    template_name = 'project-detail.html'

    def get_queryset(self):
        return Project.objects.all().prefetch_related('areas', 'areas__tasks', 'areas__project')

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['area_form'] = CreateAreaForm()
        context['task_form'] = CreateTaskForm()
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("task:project-list")
    template_name = "delete-project.html"


# AREA CRUD
class AreaCreateView(CreateView):
    form_class = CreateAreaForm
    # fields = ["name", "project"]
    template_name = "add-area.html"
    success_url = "/"


# TASK CRUD

class TaskCreateView(CreateView):
    form_class = Task
    template_name = 'add-task.html'
    # fields = ['area', 'name', 'debut', 'fin', ]


class TaskDetailView(DetailView):
    #model = Task
    template_name = 'task-detail.html'

    def get_queryset(self):
        queryset = Task.objects.all().select_related("area", "area__project")
        return queryset

    def get_sum(self, my_sum=0):
        for tool in self.object.tools.all():
            my_sum += tool.get_total()
        return my_sum

    


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["complete", ]
    template_name = 'add-task.html'
