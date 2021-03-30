from django.db import models


class Signup(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    streetno = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)

    def __str__(self):
        return self.email
