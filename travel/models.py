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

########### For places to go ##############
class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    rating = models.IntegerField()
    description = models.TextField()
    photo = models.TextField()

    def __str__(self):
        return self.name
###########################################

############ For more informations to customers #################
class Extrafunctions(models.Model):
    transpotation = models.CharField(max_length=30)
    meal = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.transpotation
###########################################

