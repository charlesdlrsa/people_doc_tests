import requests
from datetime import datetime

city_name = input('Enter the name of the city whose wether you are interested in :')
date = datetime.today().strftime('%Y/%m/%d')

response_city = requests.get('http://www.metaweather.com/api/location/search/?query={}'.format(city_name)).json()
while response_city == []:
    city_name = input('Please, enter the name of a city that exists :')
    response_city = requests.get('http://www.metaweather.com/api/location/search/?query={}'.format(city_name)).json()
city_woeid = response_city[0]['woeid']

response_weather = requests.get('https://www.metaweather.com/api/location/%s/%s' % (city_woeid, date)).json()
today_weather_state_names = list(map(lambda x: x['weather_state_name'], response_weather))

rainy_weather_state_names = ['Heavy Rain', 'Light Rain', 'Showers']

if any(state in rainy_weather_state_names for state in today_weather_state_names):
    print("It is going to rain today in %s." % city_name.capitalize())
else:
    print("It is not going to rain today in %s." % city_name.capitalize())
