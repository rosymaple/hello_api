import requests

try:
    # try-except block for error handling with requests
    # prints error message if there is a problem with the request
    response = requests.get("https://catfact.ninja/fact")

    response.raise_for_status() # raise error exception for 400/500 status codes
    print(response.status_code) # http status code to debug server issues
    print(response.text)  # json string data
    print(response.json())  # we need to turn json string data into python object

    data = response.json()

    fact = data["fact"] # access only "fact" from dictionary
    print(f'A random cat fact: {fact}') 

except Exception as e:  # catch exception errors
    print(e)
    print('There was an error making the request')

