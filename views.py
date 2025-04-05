from django.http import JsonResponse
from django.shortcuts import render  # Import only necessary functions


def flight_list(request):
    return JsonResponse({"message": "Flight list endpoint"})
