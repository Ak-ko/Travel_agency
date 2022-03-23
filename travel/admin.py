from django.contrib import admin
from .models import Booking
from users.models import UserFacts

admin.site.register(Booking)
admin.site.register(UserFacts)
