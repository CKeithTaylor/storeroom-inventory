from django.http.response import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import UpdateView, ListView, FormView, DetailView, CreateView
from django.contrib import messages
from inventory.forms import InventoryUpdateForm, StartForm, OrderForm
from inventory.models import Inventory, Order


def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def capture_data(request, *arg, **kwargs):
    if request.method == "POST":
        user_entered_loc = request.POST.get("storage_loc", None).upper()
        link = request.POST.get("link", None)
        try:
            item = Inventory.objects.get(storage_loc=user_entered_loc)
            return HttpResponseRedirect(f"/{link}/{item.id}")
        except ObjectDoesNotExist:
            messages.error(request, "Enter a valid part number")
            return HttpResponseRedirect(f"/{link}")


class InventoryStart(FormView):
    model = Inventory
    form_class = StartForm
    template_name = "inventory_start.html"


class Inventory_view(ListView):
    model = Inventory
    template_name = "inventory_view.html"


class Inventory_update(UpdateView):
    model = Inventory
    form_class = InventoryUpdateForm
    template_name = "inventory_update.html"
    success_url = reverse_lazy("inventory_start")


class Part_view(FormView):
    model = Inventory
    form_class = StartForm
    template_name = "part_view.html"


class Part_control_view(DetailView):
    model = Inventory
    template_name = "part_control.html"

    def post(self, request, *args, **kwargs):
        amount = self.request.POST.get("number")
        item = self.request.POST.get("item")
        change = self.request.POST.get("change")
        obj = Inventory.objects.get(storage_loc=item)
        if change == "add":
            obj.in_stock = F("in_stock") + amount
            obj.save()
        elif change == "remove":
            obj.in_stock = F("in_stock") - amount
            obj.save()
        return redirect(f"/part_control/{obj.id}")


class Purchase_orders(ListView):
    model = Order
    template_name = "purchase_orders.html"


class New_order(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "new_order.html"
    success_url = reverse_lazy("purchase_orders.html")
