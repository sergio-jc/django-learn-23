from rest_framework.serializers import ModelSerializer
from restaurants.models import Dish, Restaurant, Menu
# from drf_extra_fields.fields import Base64ImageField


class DishSerializer(ModelSerializer):
    # add image with base24 format
    # image = Base64ImageField(required=False)
    class Meta:
        model = Dish
        fields = ["id", "name", "description", "price", "type", "image"]


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
        # sergio-02 : print de request en el serializer create 
        context_request = self.context["request"]
        print("request context => \n", context_request)
        restaurant = Restaurant.objects.get(pk=self.initial_data["restaurant"])
        validated_data["restaurant"] = restaurant
        return Menu.objects.create(**validated_data)

    def update(self, instance, validated_data):
        dish_ids = [dish["id"] for dish in self.initial_data["menu_item"]]
        instance.menu_item.set(dish_ids)
        return super().update(instance, validated_data)
