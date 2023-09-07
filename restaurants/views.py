from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from restaurants.models import Dish, Restaurant
from restaurants.serializer import DishSerializer, RestaurantSerializer
from restaurants.permissions import IsAdminOrChefOrReadOnly, IsAdminOrReadOnly


class DishListCreateApiView(APIView):
    permission_classes = [IsAdminOrChefOrReadOnly]

    def get(self, request):
        dishes = DishSerializer(Dish.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=dishes.data)

    def post(self, request):
        created_dish = DishSerializer(data=request.data)
        if created_dish.is_valid():
            created_dish.save()
            return Response(created_dish.data)

        return Response(created_dish.errors, status=status.HTTP_400_BAD_REQUEST)


class DishRetraiveUpdateDeleteApiView(APIView):
    permission_classes = [IsAdminOrChefOrReadOnly]

    def get(self, request, pk):
        finded_dish = DishSerializer(Dish.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=finded_dish.data)

    def patch(self, request, pk):
        finded_dish = DishSerializer(
            Dish.objects.get(pk=pk), data=request.data, partial=True
        )
        if finded_dish.is_valid():
            finded_dish.save()
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
        finded_dish = Dish.objects.get(pk=pk)
        finded_dish.delete()
        return Response(
            {"mensaje": "Plato eliminado correctamente"},
            status=status.HTTP_202_ACCEPTED,
        )


class RestaurantListCreateApiVie(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]


class RestaurantRetraiveUdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]