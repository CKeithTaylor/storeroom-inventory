from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("capture_data", views.capture_data, name="capture_data"),
    path("inventory_view", views.Inventory_view.as_view(), name="inventory_view"),
    path("inventory_start", views.InventoryStart.as_view(), name="inventory_start"),
    path(
        "inventory_update/<pk>/",
        views.Inventory_update.as_view(),
        name="inventory_update",
    ),
    path("part_view", views.Part_view.as_view(), name="part_view"),
    path("part_control/<pk>/", views.Part_control_view.as_view(), name="part_control"),
    path("purchase_orders", views.Purchase_orders.as_view(), name="purchase_orders"),
    path("new_order", views.New_order.as_view(), name="new_order"),
]
