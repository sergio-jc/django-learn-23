from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=225, unique=True)
    capacity = models.IntegerField(default=30, blank=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=225, unique=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    APPETIZER = "APPETIZER"
    BEVERAGE = "BEVERAGE"
    MAIN_COURSE = "MAIN_COURSE"
    DESSERT = "DESSERT"
    SIDE = "SIDE"
    OTHER = "OTHER"
    TYPE_CHOICES = (
        (APPETIZER, "appetizer"),
        (BEVERAGE, "beverage"),
        (MAIN_COURSE, "main Course"),
        (DESSERT, "dessert"),
        (SIDE, "side"),
        (OTHER, "other"),
    )
    name = models.CharField(max_length=225, unique=True)
    description = models.TextField(blank=True, null=True, default="")
    price = models.IntegerField(blank=True, default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=OTHER)
    menu = models.ManyToManyField(Menu, related_name="menu_item")
    image = models.ImageField(blank=True, upload_to='dish/images/')

    def __str__(self):
        return self.name
