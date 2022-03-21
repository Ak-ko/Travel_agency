from django.db import models
from django.contrib.auth.models import User

class UserFacts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    identitynumber = models.CharField(max_length=25)
    visa = models.CharField(max_length=100, default=0)
    cvv = models.CharField(max_length=10, default=0)
    