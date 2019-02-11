from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from taskmanagment.models import Project, Tool, Task, Area
from .forms import CreateTaskForm, CreateProjectForm
# Create your views here.


def ProjectView(request):
    project = Project.objects.all()
    template = 'project.html'
    return render(request, template, {'project': project})


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
        context['form'] = CreateProjectForm()
        return context


class ProjectDetailView(DetailView):
    #model = Project
    template_name = 'project-detail.html'

    def get_queryset(self):
        return Project.objects.all().prefetch_related('areas__tasks')

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['form'] = CreateTaskForm()
        return context


class AreaCreateView(CreateView):
    model = Area
    fields = ["name", "project"]
    template_name = "add-area.html"

class TaskCreateView(CreateView):
    model = Task
    template_name = 'add-task.html'
    fields = ['area', 'name', 'debut', 'fin', ]


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task-detail.html'


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["complete", ]
    template_name = 'add-task.html'
