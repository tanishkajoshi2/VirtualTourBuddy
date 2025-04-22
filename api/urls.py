from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend_flights, name='recommend_flights'),  # Your flight recommendation API
    path('test/', views.test_api, name='test_api'),  # Test endpoint
]
