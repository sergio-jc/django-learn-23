from rest_framework.serializers import ModelSerializer
from restaurants.models import Dish, Restaurant


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ["id", "name", "description", "price", "type"]


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "capacity"]
