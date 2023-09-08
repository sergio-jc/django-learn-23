from rest_framework.serializers import ModelSerializer
from restaurants.models import Dish, Restaurant, Menu


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ["id", "name", "description", "price", "type"]


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "capacity"]


class MenuSerializer(ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    menu_item= DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "name", "updated_at", "restaurant", "menu_item"]

    def create(self, validated_data):
        restaurant = Restaurant.objects.get(pk=self.initial_data['restaurant'])
        validated_data['restaurant'] = restaurant
        return Menu.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        menu_items_ids = self.initial_data['menu_item']
        Menu.menu_item.clear()
        Menu.menu_item.set(menu_items_ids)
        return super().update(instance, validated_data)