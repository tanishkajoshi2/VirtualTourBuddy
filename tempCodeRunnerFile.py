from django.shortcuts import render
from rest_framework import viewsets
from api.models import Flight
from api.serializers import FlightSerializer 


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
