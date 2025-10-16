import os
import requests
from pprint import pprint
from datetime import datetime

key = os.environ.get('WEATHER_KEY')

# access enviornment variable for api key

# parameters needed from API data
# we don't need to read everything from the API
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
for forecast in list_of_forecasts: # iterate through list of dictionaries
    temp = forecast['main']['temp']
    timestamp = forecast['dt'] # unix timestamp
    forecast_date = datetime.fromtimestamp(timestamp) # converts unix seconds to local datetime
    print(temp, forecast_date)
    print(f'At {forecast_date} the temperature will be {temp}°F')

