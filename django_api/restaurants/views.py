import random 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.utils import IntegrityError

from .models import Restaurant
from .serializers import RestaurantSerializer


class GetAllRestaurantsOrCreateOneView(APIView):

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        restaurant_name = request.data.get('name')
        try:
            restaurant = Restaurant(name=restaurant_name)
            restaurant.save()
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        except IntegrityError:
            return Response("You must provide a correct name for the restaurant", 400)


class DeleteRestaurantView(APIView):

    def delete(self, request, name):
        try:
            restaurant = Restaurant.objects.get(name=name)
            restaurant.delete()
            return Response("Your restaurant was deleted")
        except Restaurant.DoesNotExist:
            return Response("You can only delete an existing restaurant", 400)


class GetRandomRestaurantView(APIView):

    def get(self, request):
        restaurant = Restaurant.objects.order_by('?').first()
        if restaurant:
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        else: 
            return Response("No restaurants are registered.")