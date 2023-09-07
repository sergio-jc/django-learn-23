from django.contrib import admin
from restaurants.models import Restaurant, Dish, Menu


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "capacity"]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "price"]


admin.site.register(Menu)