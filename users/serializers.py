from rest_framework.serializers import ModelSerializer
from users.models import Consumer, Employee
from django.contrib.auth.models import User

class BasicUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]


class ConsumerSerializer(ModelSerializer):
    user = BasicUserSerializer(read_only=True)
    class Meta:
        model = Consumer
        fields = ["type", "user"]


class EmployeeSerializer(ModelSerializer):
    user = BasicUserSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = ["role", "user"]
