from django.db import models
from django.contrib.auth.models import User

# class Customer(models.Model):
#     username = models.CharField(max_length=20)
#     phonenumber = models.CharField(max_length=20)
#     email = models.TextField()
#     identitynumber = models.CharField(max_length=30)
#     password = models.CharField(max_length=100)
#     visa = models.CharField(max_length=100, default=0)
#     cvv = models.CharField(max_length=10, default=0)

#     def __str__(self):
#         return self.username

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
