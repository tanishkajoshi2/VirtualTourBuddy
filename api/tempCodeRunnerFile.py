import requests
from django.conf import settings

def get_flight_data(departure_city, arrival_city, departure_date, return_date):
    # URL to make the API call with the provided parameters
    url = f'https://api.flightapi.io/roundtrip/{settings.FLIGHT_API_KEY}/{departure_city}/{arrival_city}/1/{departure_date}/{return_date}/1/0/0'
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the flight data as JSON
    else:
        return None  # If there is an error, return None

