from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight
from django.db.models import Q

def home(request):
    return HttpResponse("Welcome to the Flight Booking System!")

def recommend_flights(request):
    # Get query parameters from the URL
    departure_city = request.GET.get('departure_city')
    arrival_city = request.GET.get('arrival_city')
    max_price = request.GET.get('max_price')
    flight_class = request.GET.get('flight_class')
    is_direct = request.GET.get('is_direct')

    # Start by getting all flights
    flights = Flight.objects.all()

    # Apply filters if provided
    if departure_city:
        flights = flights.filter(departure_city__iexact=departure_city)
    
    if arrival_city:
        flights = flights.filter(arrival_city__iexact=arrival_city)
    
    if max_price:
        try:
            max_price = float(max_price)
            flights = flights.filter(price__lte=max_price)
        except ValueError:
            return HttpResponse("Invalid max_price value, must be a number.", status=400)
    
    if flight_class:
        if flight_class not in ['economy', 'business', 'first']:
            return HttpResponse("Invalid flight_class value. Must be 'economy', 'business', or 'first'.", status=400)
        flights = flights.filter(flight_class=flight_class)
    
    if is_direct is not None:
        if is_direct.lower() == 'true':
            flights = flights.filter(is_direct=True)
        elif is_direct.lower() == 'false':
            flights = flights.filter(is_direct=False)
        else:
            return HttpResponse("Invalid value for 'is_direct', must be 'true' or 'false'.", status=400)

    # Render the recommendations page with the filtered flights
    return render(request, 'flights/recommendations.html', {'flights': flights})
