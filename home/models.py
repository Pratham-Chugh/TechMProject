from django.db import models

# Create your models here.
class donation_data(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    cause = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    ifsc = models.IntegerField()
