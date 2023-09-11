from django.db import models
from restaurants.models import Dish


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField(default=1, blank=True)
    location = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False, blank=True)
    dishes = models.ManyToManyField(
        Dish, related_name="order_item", through="OrderItem", blank=True
    )

    def __str__(self):
        return f"Order for Table {self.table} at {self.created_at}"


class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.dish.name} in Order {self.order.id}"
