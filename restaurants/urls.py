from django.urls import path
from restaurants.views import *

urlpatterns = [
    path("dish/", DishListCreateApiView.as_view()),
    path("dish/<int:pk>/", DishRetraiveUpdateDeleteApiView.as_view()),
    path("restaurant/", RestaurantListCreateApiVie.as_view()),
    path("restaurant/<int:pk>/", RestaurantRetraiveUdateDeleteApiView.as_view()),
    path("menu/", MenuListCreateApiView.as_view()),
    path("menu/<int:pk>", MenuRetraiveUdateDeleteApiView.as_view() )
]
