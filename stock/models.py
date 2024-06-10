from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class Stock(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_weight = models.DecimalField(max_digits=3, decimal_places=2)


    def __str__(self):
        return f"Produkt: {self.name}"



