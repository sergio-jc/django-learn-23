from django.shortcuts import render
from rest_framework import generics, permissions
from users.models import *
from users.serializers import *


class UserListApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = BasicUserSerializer


class UserRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = BasicUserSerializer


class ConsumerListApiView(generics.ListAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class ConsumerRetrieveApiView(generics.RetrieveAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
