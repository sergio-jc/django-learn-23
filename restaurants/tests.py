from faker import Faker
from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from rest_framework import status

from users.init_groups import init_groups
from restaurants.models import Dish
from restaurants.fake_data_generators import dish_fake_data

fake = Faker()

# sergio-05 : test para un modelo para todas los métodos usando APITestCase
class DishTestApiView(APITestCase):
    url = "/api/dish/"

    def setUp(self):
        init_groups()
        dish_fake_data.generate_dishes(testing_environment=True)

        created_user = User.objects.create_user("developer", "developer")
        chef_group = Group.objects.get(pk=1)
        created_user.groups.add(chef_group)
        self.user = created_user
        self.client.force_authenticate(created_user)
        return super().setUp()

    def test_get_all_dishes(self):
        response = self.client.get(self.url)
        dish_count = Dish.objects.all().count()
        self.assertEqual(len(response.data), dish_count)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_dish(self):
        created_dish = Dish.objects.create(name=fake.word())
        response = self.client.get(self.url + str(created_dish.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), created_dish.id)

    def test_create_dish(self):
        data = {
            "name": fake.word(),
            "description": fake.text(),
            "price": 5000,
            "type": "MAIN_COURSE",
        }
        prev_dishes_count = Dish.objects.all().count()
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), data.get("name"))
        self.assertEqual(Dish.objects.all().count(), prev_dishes_count + 1)

    def test_update_dish(self):
        data = {"name": "test"}
        created_dish = Dish.objects.create(name=fake.word())
        response = self.client.patch(
            self.url + str(created_dish.id) + "/", data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data.get("name"), created_dish.name)

    def test_delete_dish(self):
        created_dish = Dish.objects.create(name=fake.word())
        prev_dishes_count = Dish.objects.all().count()
        response = self.client.delete(self.url + str(created_dish.id) + "/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dish.objects.all().count(), prev_dishes_count - 1)


