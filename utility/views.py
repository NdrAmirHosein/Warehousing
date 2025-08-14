from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Utilities, Warehouse, GroupType, Product, UsageType
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    )


class AddUtility(CreateView):
    model = Utilities
    fields = ["utility_name"]
    template_name = "utilities.html"
    success_url = reverse_lazy("utilities")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Utilities.objects.all()
        return context

class UtilityDelete(DeleteView):
    model = Utilities
    success_url = reverse_lazy("utilities")

    def get(self):
        return redirect(self.success_url)
    
class UtilityUpdate(UpdateView):
    model = Utilities
    fields = ["utility_name"]
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("utilities")
    

class WarehouseAdd(CreateView):
    model = Warehouse
    template_name = "warehouses.html"
    success_url = reverse_lazy("warehouses")

    fields = [
        "warehouse_code",
        "warehouse_name",
        "phone_number",
        "address",
              ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Warehouse.objects.all()
        return context
    
class WarehouseDelete(DeleteView):
    model = Warehouse
    success_url = reverse_lazy("warehouses")

    def get(self):
        return redirect(self.success_url)
    
class WarehouseUpdate(UpdateView):
    model = Warehouse
    template_name = "warehouses.html"
    fields = [
        "warehouse_code",
        "warehouse_name",
        "phone_number",
        "address",
              ]
    
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("warehouses")

class GroupeTypeAdd(CreateView):
    model = GroupType
    template_name = "group_type.html"
    success_url = reverse_lazy("group-types")

    fields = [
        "group_name"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = GroupType.objects.all()
        return context
    
class GroupTypeDelete(DeleteView):
    model = GroupType
    success_url = reverse_lazy("group-types")

    def get(self):
        redirect(self.success_url)

class GroupTypeUpdate(UpdateView):
    model = GroupType
    template_name = "group_type.html"

    fields = [
        "group_name",
    ]

    pk_url_kwarg = "pk"
    success_url = reverse_lazy("group-types")



    
class UsageTypeAdd(CreateView):
    model = UsageType
    template_name = 'usage_type.html'
    success_url = reverse_lazy("usage-type")

    fields = [
        "usage_type"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = UsageType.objects.all()
        return context

class UsageTypeDelete(DeleteView):
    model = UsageType
    success_url = reverse_lazy("usage-type")

    def get(self):
        redirect(self.success_url)

class UsageTypeUpdate(UpdateView):
    model = UsageType

    fields = [
        "usage_type"
    ]

    pk_url_kwarg = "pk"
    success_url = reverse_lazy("usage-type")
class ProductAdd(CreateView):
    model = Product
    template_name = 'products.html'
    success_url = reverse_lazy("products")
    
    fields = [
        'product_code',
        'product_name',
        'product_abbreviation_code',
        'product_unit',
        'product_group',
        'product_place',
        'buy_price',
        'sell_price',
        'registration_date',
        'usage_type',
        'description',
    ]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.all()
        return context
    
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy("products")

    def get(self):
        redirect(self.success_url)

class ProductUpdate(UpdateView):
    model = Product
    template_name = "products.html"
    success_url = reverse_lazy("products")

    fields = [
        'product_code',
        'product_name',
        'product_abbreviation_code',
        'product_unit',
        'product_group',
        'product_place',
        'buy_price',
        'sell_price',
        'registration_date',
        'usage_type',
        'description',
    ]

    pk_url_kwarg = "pk"



def main(request):
    return render(request, "main.html")

def master(request):
    return render(request, "master.html")
