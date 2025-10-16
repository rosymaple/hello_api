import requests
from pprint import pprint
import os

key = os.environ.get('WEATHER_KEY')
print(key)

url = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter city name: ')
country = input('Enter 2 character country code: ')
location = f'{city},{country}'

query = {
    'q':
    location,
    'units': 'imperial',
    'appid': key
}

data = requests.get(url, params=query).json()

pprint(data) # pretty print JSON data

temp = data['main']['temp'] # need to access nested dictionary
print(f'The current temperature is {temp}°F')

