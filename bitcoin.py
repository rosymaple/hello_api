import requests
from pprint import pprint

coindesk_url = "https://claraj.github.io/mock-bitcoin/currentprice.json"

response = requests.get(coindesk_url)
data = response.json()  # return python object for our program to use
pprint(data) # pretty print JSON response

dollars_exchange_rate = data["bpi"]["USD"]["rate"]  # nested dictionary access
print(f"Bitcoin price in dollars: ${dollars_exchange_rate}")

bitcoin = float(input('Enter the number of bitcoins: '))
bitcoin_value_in_dollars = bitcoin * float(dollars_exchange_rate) # can't multiply different value types

print(f'{bitcoin} bitcoin is equivalent to ${bitcoin_value_in_dollars}')
# final computation and output