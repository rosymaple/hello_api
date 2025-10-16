import requests

try:
    response = requests.get("https://catfact.ninja/fact")

    response.raise_for_status() # raise error exception for 400/500 status codes
    print(response.status_code)
    print(response.text)
    print(response.json())

    data = response.json()

    fact = data["fact"]
    print(f'A random cat fact: {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request')

