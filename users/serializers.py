from rest_framework import serializers
from users.models import Consumer, Employee
from django.contrib.auth.models import User, Group


class BasicUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]

    def create(self, validated_data):
        user_created = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        user_created.first_name = validated_data["first_name"]
        user_created.last_name = validated_data["last_name"]
        user_created.save()
        Consumer.objects.create(user=user_created, type=Consumer.NORMAL)
        return user_created


class ConsumerSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)

    class Meta:
        model = Consumer
        fields = ["type", "user"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["role", "user"]

    def create(self, validated_data):
        employee_created = super().create(validated_data)
        user = validated_data["user"]
        if employee_created.role == "CHEF":
            chef_group = Group.objects.get(pk=1)
            user.groups.add(chef_group)

        if employee_created.role == "WAITER":
            waiter_group = Group.objects.get(pk=2)
            user.groups.add(waiter_group)

        return employee_created
