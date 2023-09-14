from django.urls import path
from users.views import *

urlpatterns = [
    path("user/", UserListApiView.as_view()),
    path("user/<int:pk>/", UserRetrieveApiView.as_view()),
    path("consumer/", ConsumerListApiView.as_view()),
    path("consumer/<int:pk>/", ConsumerRetrieveApiView.as_view()),
    path("employee/", EmployeeListCreateAPIView.as_view()),
    path("employee/<int:pk>", EmployeeRetrieveApiView.as_view()),
]
