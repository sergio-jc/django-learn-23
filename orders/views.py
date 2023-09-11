from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

# from django_filters.rest_framework import DjangoFilterBackend
from orders.models import *
from orders.serializers import *
from orders.permissions import IsWaiter

# from restaurants.permissions import IsAdminOrChefOrReadOnly, IsAdminOrReadOnly


class TableListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsWaiter]
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsWaiter]
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OrderlistCreateApiView(generics.ListAPIView):
    permission_classes = [IsWaiter]
    queryset = Order.objects.all()
    serializer_class = BasicOrderSerializer


class OrderRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsWaiter]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
