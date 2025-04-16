import requests
from django.http import JsonResponse

API_KEY = '67db2e9d905be30e6d08de35'  # Replace with your actual API key

def test_api(request):
    return JsonResponse({'message': 'Test API is working!'}) 

def recommend_flights(request):
    origin = request.GET.get('departure', 'DEL')
    destination = request.GET.get('arrival', 'BLR')
    departure_date = request.GET.get('departure_date', '2025-06-01')  # YYYY-MM-DD
    adults = request.GET.get('adults', 1)
    children = request.GET.get('children', 0)
    infants = request.GET.get('infants', 0)
    cabin_class = request.GET.get('cabin_class', 'economy')
    currency = request.GET.get('currency', 'INR')

    # Construct the URL for the Oneway Trip Pricing API
    url = f"https://api.flightapi.io/onewaytrip/{API_KEY}/{origin}/{destination}/{departure_date}/{adults}/{children}/{infants}/{cabin_class}/{currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        flight_data = response.json()

        return JsonResponse(flight_data, safe=False)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
