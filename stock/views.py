from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestockForm
from .models import Supply
from django.views.generic import UpdateView
# Create your views here.


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
            return redirect("project_list")
    return render(request, "restock.html", {"form": form})
