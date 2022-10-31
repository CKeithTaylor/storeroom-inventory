from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone, dateformat
from django.urls import reverse
from datetime import date


class Inventory(models.Model):
    class Meta:
        db_table = "inventory"
        managed = True

    storage_loc = models.CharField(max_length=12, blank=True, null=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    part = models.CharField(max_length=50, blank=True, null=True)
    vendor = models.CharField(max_length=50, blank=True, null=True)
    in_stock = models.IntegerField(default=0, blank=True, null=True)
    max_stock = models.IntegerField(default=0, blank=True, null=True)
    reorder = models.IntegerField(default=0, blank=True, null=True)
    reorder_amt = models.IntegerField(default=0, blank=True, null=True)
    location = models.CharField(default="DSO", max_length=50, blank=True, null=True)
    inv_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("inventory_update", kwargs={"pk": self.id})


class Order(models.Model):
    class Meta:
        db_table = "orders"
        managed = True
        ordering = ["-order_date"]

    part = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    order_date = models.DateField(default=date.today(), blank=False)
    receive_date = models.DateField(default=date.today(), blank=False)
    invoice = models.CharField(max_length=64, default="", blank=True, null=True)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    cost = models.IntegerField(default=1, blank=True, null=True)
    tax = models.IntegerField(default=1, blank=True, null=True)
    shipping = models.IntegerField(default=1, blank=True, null=True)
    total = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("purchase_orders", kwargs={"pk": self.id})
