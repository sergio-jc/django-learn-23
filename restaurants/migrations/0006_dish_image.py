# Generated by Django 4.2.5 on 2023-09-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_custom_empty_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, upload_to='dish/images/'),
        ),
    ]