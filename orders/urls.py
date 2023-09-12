from django.urls import path
from orders.views import *


urlpatterns = [
    path("html/", index),
    path("table/", TableListCreateApiView.as_view()),
    path("table/<int:pk>/", TableRetrieveUpdateDeleteApiView.as_view()),
    path("order/", OrderlistCreateApiView.as_view()),
    path("order/<int:pk>/", OrderRetrieveUpdateDeleteApiView.as_view()),
]