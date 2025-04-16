from django.contrib import admin
from django.urls import path, include
from flights import views  # Import views from the flights app

urlpatterns = [
    path('admin/', admin.site.urls),                 # Admin panel URL
    path('api/', include('api.urls')),               # Include API URLs
    path('flights/', include('flights.urls')),       # Handle /flights/ routes
    path('', views.home, name='home'),               # Homepage route
]



