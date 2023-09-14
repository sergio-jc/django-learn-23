from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from restaurants.models import Dish, Restaurant, Menu
from restaurants.serializers import *
from restaurants.permissions import IsChef
from restaurants.custom_list_create import CustomListCreateAPIView
from django.utils.translation import gettext as _


def dish_list_html(request):
    dishes = DishSerializer(Dish.objects.all(), many=True).data
    context = {"dishes": dishes}

    return render(request, "dish_list.html", context)


class DishListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsChef]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["type"]
    search_fields = ["name"]
    ordering_fields = ["price"]


class DishRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsChef]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantListCreateApiView(CustomListCreateAPIView):
    permission_classes = [IsChef]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name"]
    ordering_fields = ["capacity"]
    pagination_class = LimitOffsetPagination


class RestaurantRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsChef]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = [IsAdminOrReadOnly]


class MenuListCreateApiView(CustomListCreateAPIView):
    permission_classes = [IsChef]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class MenuRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsChef]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# API View example :

# class DishListCreateApiView(APIView):

#     def get(self, request):
#         dishes = DishSerializer(Dish.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=dishes.data)

#     def post(self, request):
#         created_dish = DishSerializer(data=request.data)
#         if created_dish.is_valid():
#             created_dish.save()
#             return Response(created_dish.data)

#         return Response(created_dish.errors, status=status.HTTP_400_BAD_REQUEST)


# class DishRetrieveUpdateDeleteApiView(APIView):

#     def get(self, request, pk):
#         found_dish = DishSerializer(Dish.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=found_dish.data)

#     def patch(self, request, pk):
#         found_dish = DishSerializer(
#             Dish.objects.get(pk=pk), data=request.data, partial=True
#         )
#         if found_dish.is_valid():
#             found_dish.save()
#             return Response(
#                 {"mensaje": "Plato actualizado"},
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return Response(
#                 {"mensaje": "El plato no se actualizo"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#     def delete(self, request, pk):
#         found_dish = Dish.objects.get(pk=pk)
#         found_dish.delete()
#         return Response(
#             {"mensaje": "Plato eliminado correctamente"},
#             status=status.HTTP_202_ACCEPTED,
#         )
