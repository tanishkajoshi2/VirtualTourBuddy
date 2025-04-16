from rest_framework import serializers
from api.models import Flight  # Ensure the correct model is imported

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight  # Ensure model name matches what's in models.py
        fields = '__all__'  # Correct syntax for including all fields
