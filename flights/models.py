from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, default='UNKNOWN123')
    departure_city = models.CharField(max_length=100, default='Unknown City')
    arrival_city = models.CharField(max_length=100, default='Unknown City')
    departure_time = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    flight_class = models.CharField(
        max_length=20,
        choices=[
            ('economy', 'Economy'),
            ('business', 'Business'),
            ('first', 'First Class')
        ],
        default='economy'
    )
    is_direct = models.BooleanField(default=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number}"

