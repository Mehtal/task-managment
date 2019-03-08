from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .forms import RestockForm, SendToTaskForm, SupplyForm
from .models import Supply
from django.views.generic import UpdateView, CreateView, ListView
from taskmanagment.models import Tool, Project, Area, Task
# Create your views here.


class SupplyCreateView(CreateView):
    model = Supply
    template_name = "supply-create.html"
    fields = ["name", "quantity", "unit_price"]
    success_url = reverse_lazy("stock:supply-list")


class SupplyListView(ListView):
    queryset = Supply.objects.all().order_by("name")
    template_name = "supply-list.html"


def add_supply(request, pk):
    # getting the object
    item = get_object_or_404(Supply, pk=pk)
    # instantiating the form on using initial since its not a model form
    form = RestockForm(initial={"name": item.name, "quantity": item.quantity, "unit_price": item.unit_price})
    if request.POST:
        # getting form extra input data
        new_quantity = request.POST.get("new_quantity")
        new_price = request.POST.get("new_price")
        form = RestockForm(request.POST,)
        if form.is_valid():
            old_supply = item.get_total()
            new_supply = int(new_quantity) * int(new_price)
            quantity = item.quantity + int(new_quantity)
            item.unit_price = (old_supply + new_supply) / quantity
            item.quantity = quantity
            # important need to save the object
            item.save()
            return redirect("stock:supply-list")
    return render(request, "restock.html", {"form": form})


class SupplyUpdateView(UpdateView):
    model = Supply
    # form_class = SupplyForm
    fields = ["name", "quantity", "unit_price"]
    template_name = "supply-update.html"
    success_url = reverse_lazy("stock:supply-list")


def send_supply_to_tasks(request):
    form = SendToTaskForm()
    item = Supply.objects.all()
    project = Project.objects.all()
    area = Area.objects.all()
    task = Task.objects.all()
    if request.POST:
        form = SendToTaskForm(request.POST)
        item_id = request.POST.get("name")
        project_id = request.POST.get("project")
        area_id = request.POST.get("area")
        task_id = request.POST.get("task")
        quantity = request.POST.get("quantity")
        item = Supply.objects.get(pk=item_id)
        project = Project.objects.get(pk=project_id)
        area = Area.objects.get(pk=area_id)
        task = Task.objects.get(pk=task_id)
        if form.is_valid():
            if item.quantity >= int(quantity):
                Tool.objects.create(name=item.name, quantity=quantity, unit_price=item.unit_price, task=task,)
                item.quantity -= int(quantity)
                item.save()
                messages.success(request, "vous avez envoyé {} {} à {} avec succès".format(quantity, item.name, task.name))
                return redirect(reverse("stock:supply-list"))
            else:
                messages.error(request, "lorsque vous essayez d'envoyer {} {} alors que vous n'en avez que {} en stock".format(quantity, item.name, item.quantity))
    return render(request, "supply-send.html", {"form": form, })


def load_areas(request):
    project_id = request.GET.get('project')
    areas = Area.objects.filter(project_id=project_id).order_by('name')
    return render(request, 'ajax/area_dropdown_list_options.html', {'areas': areas})


def load_tasks(request):
    area_id = request.GET.get('area')
    tasks = Task.objects.filter(area_id=area_id).order_by('name')
    return render(request, 'ajax/task_dropdown_list_options.html', {'tasks': tasks})
