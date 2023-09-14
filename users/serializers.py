from rest_framework import serializers
from users.models import Consumer, Employee
from django.contrib.auth.models import User


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
            validated_data["username"], validated_data["email"], validated_data["password"]
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
    user = BasicUserSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ["role", "user"]
