from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
# from django_filters.rest_framework import DjangoFilterBackend
from restaurants.models import Dish, Restaurant, Menu
from restaurants.serializer import DishSerializer, RestaurantSerializer, MenuSerializer
# from restaurants.permissions import IsAdminOrChefOrReadOnly, IsAdminOrReadOnly
from custom_list_create import CustomListCreateAPIView


class DishListCreateApiView(APIView):
    # permission_classes = [IsAdminOrChefOrReadOnly]

    def get(self, request):
        dishes = DishSerializer(Dish.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=dishes.data)

    def post(self, request):
        created_dish = DishSerializer(data=request.data)
        if created_dish.is_valid():
            created_dish.save()
            return Response(created_dish.data)

        return Response(created_dish.errors, status=status.HTTP_400_BAD_REQUEST)


class DishRetrieveUpdateDeleteApiView(APIView):
    # permission_classes = [IsAdminOrChefOrReadOnly]

    def get(self, request, pk):
        found_dish = DishSerializer(Dish.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=found_dish.data)

    def patch(self, request, pk):
        found_dish = DishSerializer(
            Dish.objects.get(pk=pk), data=request.data, partial=True
        )
        if found_dish.is_valid():
            found_dish.save()
            return Response(
                {"mensaje": "Plato actualizado"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"mensaje": "El plato no se actualizo"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        found_dish = Dish.objects.get(pk=pk)
        found_dish.delete()
        return Response(
            {"mensaje": "Plato eliminado correctamente"},
            status=status.HTTP_202_ACCEPTED,
        )


class RestaurantListCreateApiView(CustomListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = [IsAdminOrReadOnly]
    filter_backends = [
        # DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # filterset_fields = ['capacity']
    search_fields = ["name"]
    ordering_fields = ["capacity"]
    pagination_class = LimitOffsetPagination


class RestaurantRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = [IsAdminOrReadOnly]


class MenuListCreateApiView(CustomListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

class MenuRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer