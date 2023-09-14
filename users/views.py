from django.shortcuts import render
from rest_framework import generics, permissions
from users.models import *
from users.serializers import *
from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle


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

# sergio-08: Custom throttle class
class CustomThrottle(SimpleRateThrottle):
    scope = "custom"
    def get_cache_key(self, request, view):
        user = request.user.pk if request.user.is_authenticated else 'anon'
        # view_name = view.__class__.__name__
        # return f'custom_throttle:{user}:{view_name}'

        # how UserRateThrottle set the cache
        return self.cache_format % {
            'scope': self.scope,
            'ident': user
        }


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    throttle_classes = [CustomThrottle]
    permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
