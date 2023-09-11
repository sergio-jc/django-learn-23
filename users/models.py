from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    CHEF = "CHEF"
    WAITER = "WAITER"
    ADMIN = "ADMIN"
    OTHER = "OTHER"
    ROLE_CHOICES = (
        (CHEF, "chef"),
        (WAITER, "waiter"),
        (ADMIN, "administrator"),
        (OTHER, "other"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=OTHER)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.role} - {self.user.username}"


class Consumer(models.Model):
    NORMAL = "NORMAL"
    PREMIUM = "PREMIUM"
    OTHER = "OTHER"
    TYPE_CHOICES = (
        (NORMAL, "normal"),
        (PREMIUM, "premium"),
        (OTHER, "other"),
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=OTHER)

    def __str__(self):
        return f"{self.type} - {self.user.username}"
