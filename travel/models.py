from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    adult = models.IntegerField(5)
    kundersix = models.IntegerField(3)
    singleroom = models.IntegerField(4)
    doubleroom = models.IntegerField(2)
    familyroom = models.IntegerField(1)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.time

