# import requests
# from pprint import pprint

# coindesk_url = "https://claraj.github.io/mock-bitcoin/currentprice.json"

# response = requests.get(coindesk_url)
# data = response.json()
# pprint(data)

# dollars_exchange_rate = data["bpi"]["USD"]["rate"]
# print(f"Bitcoin price in dollars: ${dollars_exchange_rate}")

# bitcoin = float(input('Enter the number of bitcoins: '))
# bitcoin_value_in_dollars = bitcoin * dollars_exchange_rate

# print(f'{bitcoin} bitcoin is equivalent to ${bitcoin_value_in_dollars}')
