from django.conf.urls import url

from .views import GetAllRestaurantsOrCreateOneView, DeleteRestaurantView, GetRandomRestaurantView

app_name = 'restaurants'
urlpatterns = [
    # ex: /restaurants
    url(r'^/?$', GetAllRestaurantsOrCreateOneView.as_view(), name='get-all-restaurants-or-create-one'),
    # ex: /restaurants/random
    url(r'^random/?$', GetRandomRestaurantView.as_view(), name='get-random-restaurant'),
    # ex: /restaurants/KFC
    url(r'^(?P<name>\w+( +\w+)*)/?$', DeleteRestaurantView.as_view(), name='delete-restaurant'),
]