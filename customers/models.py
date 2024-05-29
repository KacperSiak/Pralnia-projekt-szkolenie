from django.conf import settings
from django.db import models

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

