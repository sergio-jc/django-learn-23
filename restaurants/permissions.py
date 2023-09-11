from rest_framework.permissions import BasePermission, DjangoModelPermissions
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


# class IsChef(DjangoModelPermissions):
#     def has_permission(self, request, view):
#         print("=> \n", self, request, view)
#         return super().has_permission(request, view)
#     perms_map = {
#         "GET": ["%(app_label)s.view%(model_name)s"],
#         "OPTIONS": [],
#         "HEAD": [],
#         "POST": ["%(app_label)s.add_%(model_name)s"],
#         "PUT": ["%(app_label)s.change_%(model_name)s"],
#         "PATCH": ["%(app_label)s.change_%(model_name)s"],
#         "DELETE": ["%(app_label)s.delete_%(model_name)s"],
#     }


class IsChef(DjangoModelPermissions):
    # def has_permission(self, request, view):
    #     user= request.user
    #     print("secio => \n",user.get_all_permissions())
    #     if user.has_perm('restaurants.view_restaurant'):
    #         return True
    #     return False

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }
