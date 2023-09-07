from django.urls import path
from restaurants.views import (
    DishRetraiveUpdateDeleteApiView,
    DishListCreateApiView,
    RestaurantListCreateApiVie,
    RestaurantRetraiveUdateDeleteApiView,
)

urlpatterns = [
    path("dish/", DishListCreateApiView.as_view()),
    path("dish/<int:pk>/", DishRetraiveUpdateDeleteApiView.as_view()),
    path("restaurant/", RestaurantListCreateApiVie.as_view()),
    path("restaurant/<int:pk>/", RestaurantRetraiveUdateDeleteApiView.as_view()),
]
