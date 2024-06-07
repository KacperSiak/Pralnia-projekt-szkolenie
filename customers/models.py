from django.conf import settings
from django.db import models

from stock.models import Stock

User = settings.AUTH_USER_MODEL


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=9)
    nip = models.CharField(max_length=11)
    contact_person = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Klient {self.name}"


class Contract(models.Model):
    number = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price_for_kg = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    stocks = models.ManyToManyField(Stock, through='ContractStock')

    def __str__(self):
        return f"Umowa o numerze {self.number}"


class Invoice(models.Model):
    number = models.CharField(max_length=100)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date_of_receipt = models.DateField()
    payment_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Umowa o numerze {self.number}"


class ContractStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    is_leased = models.BooleanField(default=False)

    def __str__(self):
        return f"Produkt: {self.stock} z umowy: {self.contract}"
