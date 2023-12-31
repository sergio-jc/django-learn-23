# Generated by Django 4.2.5 on 2023-09-12 16:14

from django.db import migrations

# sergio-04: empty migration, incrementa el precio de los platillos en un 10%
def increase_dish_price(apps, schema_editor):
    Dish = apps.get_model("restaurants", "Dish")
    for dish in Dish.objects.all():
        dish.price = dish.price + (dish.price / 10)
        dish.save()

class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_alter_dish_menu'),
    ]

    operations = [
        migrations.RunPython(increase_dish_price)
    ]
