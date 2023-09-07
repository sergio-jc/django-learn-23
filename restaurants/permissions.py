from rest_framework.permissions import BasePermission
from users.models import Employee


def isChef(request):
    user_pk = request.user.pk
    if user_pk:
        employee = Employee.objects.get(user_pk=user_pk)
        return Employee.CHEF == employee.type

    return False


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" or request.user.is_staff:
            return True
        return False


class IsAdminOrChefOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" or request.user.is_staff:
            return True
        isChef(request=request)


class IsAdminOrChef(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        isChef(request=request)
