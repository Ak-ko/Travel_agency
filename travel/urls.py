from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='travel-home'),
    path('login/', views.login, name='travel-login'),
    path('register/', views.register, name='travel-register'),
]