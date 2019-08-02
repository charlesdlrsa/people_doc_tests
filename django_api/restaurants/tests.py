from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Restaurant
from .serializers import RestaurantSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_restaurant(name):
        Restaurant.objects.create(name=name)

    def setUp(self):
        # add test data
        self.create_restaurant("macdo")
        self.create_restaurant("kfc")
        self.create_restaurant("subway")


class GetAllRestaurantsViewTest(BaseViewTest):
    def test_get_all_restaurants(self):
        """
        This test ensures that all restaurants added in the setUp method
        exist when we make a GET request to the restaurants/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("restaurants:get-all-restaurants-or-create-one")
        )
        # fetch the data from db
        expected = Restaurant.objects.all()
        serialized = RestaurantSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_restaurant(self):
        """
        This test ensures that a new restaurant is created when we make a POST 
        request to the restaurants/ endpoint
        """
        # hit the API endpoint
        response = self.client.post(
            reverse("restaurants:get-all-restaurants-or-create-one"),
            {"name": "burgerking"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Restaurant.objects.get(name="burgerking"))

    def test_create_new_restaurant_without_name(self):
        """
        This test ensures that a new restaurant is created when we make a POST 
        request to the restaurants/ endpoint
        """
        # hit the API endpoint
        response = self.client.post(
            reverse("restaurants:get-all-restaurants-or-create-one")
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteRestaurantViewTest(BaseViewTest):
    def test_delete_restaurant(self):
        """
        This test ensures that the specified restaurant is deleted when we make a DELETE 
        request to the restaurants/<name> endpoint
        """
        # hit the API endpoint
        response = self.client.delete(
            reverse("restaurants:delete-restaurant", kwargs={"name": "macdo"})
        )
        # fetch the data from db
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        restaurant = Restaurant.objects.filter(name="macdo").first()
        self.assertFalse(restaurant)

    def test_delete_restaurant_that_doesnt_exist(self):
        """
        This test ensures that the specified restaurant is deleted when we make a DELETE 
        request to the restaurants/<name> endpoint
        """
        # hit the API endpoint
        response = self.client.delete(
            reverse("restaurants:delete-restaurant", kwargs={"name": "burgerking"})
        )
        # fetch the data from db
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetRandomRestaurantViewTest(BaseViewTest):
    def test_get_random_restaurant(self):
        """
        This test ensures that a random existing restaurant is returned when we make a GET 
        request to the restaurants/random endpoint
        """
        # hit the API endpoint
        response = self.client.get(reverse("restaurants:get-random-restaurant"))
        # fetch the data from db
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = Restaurant.objects.all()
        serialized = RestaurantSerializer(expected, many=True)
        self.assertIn(response.data, serialized.data)

