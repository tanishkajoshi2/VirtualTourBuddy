from django.urls import path  # Correct import for path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Homepage route
    path('recommendations/', views.recommend_flights, name='recommend_flights'),  # Recommendations route
]



