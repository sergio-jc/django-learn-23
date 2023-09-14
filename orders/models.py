# from django.conf import settings
# from django.core.mail import send_mail
from django.db import models
from restaurants.models import Dish
from users.models import User
from django.template.loader import render_to_string

# sergio-03 : añadir traducciones
from django.utils.translation import gettext as _

# django-admin makemessage  -l es
# django-admin compilemessages


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField(default=1, blank=True)
    location = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False, blank=True)
    dishes = models.ManyToManyField(
        Dish, related_name="order_item", through="OrderItem", blank=True
    )

    def __str__(self):
        return f"Order for Table {self.table} at {self.created_at}"

    # sergio-09 : custom method para mandarle un correo al cliente.
    def send_email(self):
        subject = _("Thank you for placing your order!")
        message = _("Your order has been received and is in process.")
        footer = _("Thank you for trusting us.")
        user_name = f"{self.user.first_name} {self.user.first_name}"
        context = {
            "subject": subject,
            "message": message,
            "user_name": user_name,
            "footer": footer,
        }
        html_message = render_to_string("order_email.html", context)
        print("🚀 email enviado =>", html_message)
        # from_email = settings.EMAIL_HOST_USER
        # recipient_list = ["sergiojara0609@gmail.com"]

        # send_mail(
        #     subject,
        #     message,
        #     from_email,
        #     recipient_list,
        #     html_message=html_message,
        #     fail_silently=False,
        # )


class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.dish.name} in Order {self.order.id}"
