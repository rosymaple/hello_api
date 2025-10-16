import os
import requests
from pprint import pprint
from datetime import datetime

key = os.environ.get('WEATHER_KEY')

query = {
    'q': 'Minneapolis,US',
    'units': 'imperial',
    'appid': key
}

url = 'https://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
pprint(data) # pretty print JSON data

list_of_forecasts = data['list'] # list of dictionaries

# get 5 day forecast
for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    timestamp = forecast['dt'] # unix timestamp
    forecast_date = datetime.fromtimestamp(timestamp)
    print(temp, forecast_date)
    print(f'At {forecast_date} the temperature will be {temp}°F')

