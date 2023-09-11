from django.shortcuts import render
from rest_framework import generics, permissions
from users.models import *
from users.serializers import *


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = BasicUserSerializer


class UserRetraiveApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = BasicUserSerializer


class ConsumerListApiView(generics.ListAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class ConsumerRetraiveApiView(generics.RetrieveAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class EmployeeListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetraiveApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
