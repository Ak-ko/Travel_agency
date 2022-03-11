from django.urls import path
from . import views as travel_views

urlpatterns = [
    path('', travel_views.home, name='travel-home'),
]