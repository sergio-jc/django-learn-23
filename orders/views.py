from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
# from django_filters.rest_framework import DjangoFilterBackend
from orders.models import *
from orders.serializers import *
# from restaurants.permissions import IsAdminOrChefOrReadOnly, IsAdminOrReadOnly


class TableListCreateApiView (generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class=TableSerializer


class TableRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class=TableSerializer


class OrderlistCreateApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = BasicOrderSerializer


class OrderRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class=OrderSerializer