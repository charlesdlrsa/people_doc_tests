from django.urls import path

from .views import GetAllRestaurantsView, DeleteRestaurantView, GetRandomRestaurantView

app_name = 'restaurants'
urlpatterns = [
    # ex: /restaurants/
    path('', GetAllRestaurantsView.as_view(), name='get-all-restaurants'),
    # ex: /restaurants/random/
    path('random/', GetRandomRestaurantView.as_view(), name='get-random-restaurant'),
    # ex: /restaurants/KFC/
    path('<str:name>/', DeleteRestaurantView.as_view(), name='delete-restaurant'),
]