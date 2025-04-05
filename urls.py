from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flights.urls')),  # Ensure 'flights' has a urls.py file
    path("api/v1/", include('api.urls')),  # Ensure 'api' has a urls.py file
]
