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
    menu_item = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "name", "updated_at", "restaurant", "menu_item"]

    def create(self, validated_data):
        context_request = self.context['request']
        print('request context => \n', context_request)
        restaurant = Restaurant.objects.get(pk=self.initial_data["restaurant"])
        validated_data["restaurant"] = restaurant
        return Menu.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # print("🚀 => \n", self.initial_data["menu_item"])
        dish_ids = [dish['id'] for dish in self.initial_data["menu_item"]]
        instance.menu_item.set(dish_ids)
        return super().update(instance, validated_data)
