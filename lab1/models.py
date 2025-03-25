from unittest.mock import mock_open
from django.contrib.auth.models import User

from django.db import models


# Create your models here.

class Market(models.Model):
    name = models.CharField(max_length=50)
    workingTeam = models.IntegerField
    dateOpen = models.DateField()
    workingHoursFrom = models.TimeField()
    workingHoursTo = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}" #За маркетите во листата се прикажуваат само нивните имиња


class Employee(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    embg = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # корисник кој што го додал неговата плата.

    def __str__(self):
        return f"{self.name} {self.surname}"

class ContactInfo(models.Model):
    street = models.CharField(max_length=20)
    addressNumber = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    market = models.OneToOneField(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street} {self.adressNumber} {self.phone} {self.email}"




class Product(models.Model):
    TYPE_CHOICES = [
        ("F", "Food"),
        ("D", "Drink"),
        ("B", "Bakery"),
        ("C", "Cosmetic"),
        ("H", "Hygiene")

    ]
    name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    homeMade = models.BooleanField(default=False)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
         return f"{self.name} {self.code}"


class MarketProduct(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.market.name} - {self.product.name} {self.quantity}"