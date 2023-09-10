from django.urls import path
from users.views import *

urlpatterns = [
    path("user/", UserListApiView.as_view()),
    path("user/<int:pk>/", UserRetraiveApiView.as_view()),
    path("consumer/", ConsumerListApiView.as_view()),
    path("consumer/<int:pk>/", ConsumerRetraiveApiView.as_view()),
    path("employee/", EmployeeListApiView.as_view()),
    path("employee/<int:pk>", EmployeeRetraiveApiView.as_view()),
]
