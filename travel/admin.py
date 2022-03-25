from django.contrib import admin
from .models import Booking, Place
from users.models import UserFacts

admin.site.register(Booking)
admin.site.register(Place)