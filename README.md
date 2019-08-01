# API Server

To be able to request the api, you have to run the server :

```bash
$ cd django_api
$ python manage.py migrate
$ python manage.py runserver
```

You can now make the different requests by requesting these endpoints with the 'http://localhost/' prefix :
- create a restaurant : POST /restaurants/  with the body {'name': 'Burger1'}
- delete a restaurant : DELETE /restaurants/<name>/
- get all the restaurants : GET /restaurants
- get a random restaurant : GET /restaurants/random


# API consumer

To know if it's going to rain today in a city, just launch this script and follow the instructions:

```bash
$ python script_meteo.py
```
