# Generated by Django 4.2.5 on 2023-09-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
