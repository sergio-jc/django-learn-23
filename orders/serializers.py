from rest_framework import serializers
from orders.models import *
from restaurants.serializers import DishSerializer


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ["id", "name", "capacity", "location", "is_available"]


class BasicOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields = ["id", "table", "is_completed", "created_at"]


class OrderItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["dish", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    orderitem_set = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ["id", "table", "orderitem_set", "is_completed", "created_at"]
