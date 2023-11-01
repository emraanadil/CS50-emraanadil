from django.db import models

# Create your models here.
class AdminModel(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=12)

class PizzaModel(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

class CustomerModel(models.Model):
    userid = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

class OrderModel(models.Model):
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    ordereditems = models.CharField(max_length=1000)
    status = models.CharField(max_length=10,default="Pending")