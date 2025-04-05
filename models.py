from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return self.flight_number

