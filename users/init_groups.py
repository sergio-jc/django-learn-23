from django.contrib.auth.models import User, Group, Permission

# from users.models import Employee, User, Consumer

permissions = [
    "add_logentry",
    "change_logentry",
    "delete_logentry",
    "view_logentry",
    "add_permission",
    "change_permission",
    "delete_permission",
    "view_permission",
    "add_group",
    "change_group",
    "delete_group",
    "view_group",
    "add_contenttype",
    "change_contenttype",
    "delete_contenttype",
    "view_contenttype",
    "add_session",
    "change_session",
    "delete_session",
    "view_session",
    # Users
    "add_user",
    "change_user",
    "delete_user",
    "view_user",
    # Consumer
    "add_consumer",
    "change_consumer",
    "delete_consumer",
    "view_consumer",
    # Employee
    "add_employee",
    "change_employee",
    "delete_employee",
    "view_employee",
    # Dish
    "add_dish",
    "change_dish",
    "delete_dish",
    "view_dish",
    # Menu
    "add_menu",
    "change_menu",
    "delete_menu",
    "view_menu",
    # Restaurant
    "add_restaurant",
    "change_restaurant",
    "delete_restaurant",
    "view_restaurant",
    # Table
    "add_table",
    "change_table",
    "delete_table",
    "view_table",
    # Order
    "add_order",
    "change_order",
    "delete_order",
    "view_order",
    # Order Item
    "add_orderitem",
    "change_orderitem",
    "delete_orderitem",
    "view_orderitem",
]


chef_permissions = [
    "view_menu",
    "add_restaurant",
    "change_restaurant",
    "delete_restaurant",
    "view_restaurant",
    "add_dish",
    "change_dish",
    "delete_dish",
    "view_dish",
    "add_menu",
    "change_menu",
    "delete_menu",
    "view_menu",
]


waiter_permissions = [
    "view_menu",
    "view_dish",
    "view_restaurant",
    "add_table",
    "change_table",
    "delete_table",
    "view_table",
    "add_order",
    "change_order",
    "delete_order",
    "view_order",
    "add_orderitem",
    "change_orderitem",
    "delete_orderitem",
    "view_orderitem",
]


def configure_groups(group_name, permissions_array):
    created_group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print("Group created successfully \n")
        for codename in permissions_array:
            found_permission = Permission.objects.get(codename=codename)
            created_group.permissions.add(found_permission)
        print("Permissions added successfully \n")


def init_groups():
    configure_groups(group_name="Chef", permissions_array=chef_permissions)
    configure_groups(group_name="Waiter", permissions_array=waiter_permissions)
