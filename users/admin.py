from django.contrib import admin
from users.models import (Consumer, Employee)
# Register your models here.
admin.site.register(Consumer)
admin.site.register(Employee)