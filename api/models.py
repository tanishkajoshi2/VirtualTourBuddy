from django.db import models
from django.utils import timezone

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.flight_number} - {self.airline}"

# 👉 Add this below Flight class:
class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    booked_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking for {self.name} on {self.flight.flight_number}"
