from django.contrib import admin
from django.urls import path, include
from api.views import FlightViewSet
from rest_framework import routers







router= routers.DefaultRouter()
router.register(r'flights',FlightViewSet)
urlpatterns = [
    

     path('',include(router.urls)) # Ensure 'flights' has a urls.py file
]


