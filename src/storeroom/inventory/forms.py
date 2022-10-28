from django.db.models import fields
from django.forms import widgets
from .models import Inventory, Order
from django import forms


class StartForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = (
            "part",
            "storage_loc",
        )

    part = forms.CharField(widget=forms.TextInput(attrs={}))
    storage_loc = forms.CharField(widget=forms.TextInput(attrs={}))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "order_date",
            "receive_date",
            "reconcile_date",
            "purchaser",
            "quote",
            "PO",
            "invoice",
            "acct_code",
            "part",
            "quantity",
            "cost",
            "tax",
            "shipping",
            "total",
            "reason_code",
        )

    order_date = forms.DateField(widget=forms.DateInput(attrs={}))
    receive_date = forms.DateField(required=False, widget=forms.DateInput(attrs={}))
    reconcile_date = forms.DateField(required=False, widget=forms.DateInput(attrs={}))
    purchaser = forms.CharField(widget=forms.TextInput(attrs={}))
    quote = forms.CharField(required=False, widget=forms.TextInput(attrs={}))
    PO = forms.CharField(required=False, widget=forms.TextInput(attrs={}))
    invoice = forms.CharField(required=False, widget=forms.TextInput(attrs={}))
    acct_code = forms.CharField(required=False, widget=forms.TextInput(attrs={}))
    part = forms.CharField(widget=forms.TextInput(attrs={}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={}))
    cost = forms.CharField(widget=forms.TextInput(attrs={}))
    tax = forms.CharField(required=False, widget=forms.TextInput(attrs={}))
    shipping = forms.CharField(required=False, widget=forms.TextInput(attrs={}))
    total = forms.CharField(widget=forms.TextInput(attrs={}))
    reason_code = forms.CharField(widget=forms.TextInput(attrs={}))


class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = (
            "description",
            "part",
            "in_stock",
        )

    # def __init__(self, *args, **kwargs):
    #     super(InventoryUpdateForm, self).__init__(*args, **kwargs)
    #     readonly = [
    #         "description",
    #         "part",
    #     ]
    #     for field in readonly:
    #         self.fields[field].widget.attrs["readonly"] = "true"

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 24,
                "style": "vertical-align: middle;",
                "readonly": "True",
            }
        )
    )
    part = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "readonly": "True",
            }
        )
    )
    in_stock = forms.CharField(widget=forms.TextInput(attrs={}))
