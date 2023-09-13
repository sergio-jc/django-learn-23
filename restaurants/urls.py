from django.urls import path
from restaurants.views import *

urlpatterns = [
    path("dish/", DishListCreateApiView.as_view()),
    path("dish/html", dish_list_html),
    path("dish/<int:pk>/", DishRetrieveUpdateDeleteApiView.as_view()),
    path("restaurant/", RestaurantListCreateApiView.as_view()),
    path("restaurant/<int:pk>/", RestaurantRetrieveUpdateDeleteApiView.as_view()),
    path("menu/", MenuListCreateApiView.as_view()),
    path("menu/<int:pk>", MenuRetrieveUpdateDeleteApiView.as_view()),
]
