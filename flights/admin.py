from django.contrib import admin
from .models import Flight
from .models import Booking

admin.site.register(Flight)
admin.site.register(Booking)