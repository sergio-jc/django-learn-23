# Generated by Django 4.2.5 on 2023-09-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='capacity',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]