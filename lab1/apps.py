from django.apps import AppConfig
from .models import Market, Product, Employee, ContactInfo, MarketProduct;

class Lab1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "lab1"
