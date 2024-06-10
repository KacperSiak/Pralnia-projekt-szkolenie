from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=8)
    technical_review_date = models.DateField(max_length=10)
    insurance_date = models.DateField(max_length=10)

    def __str__(self):
        return f"Samochód: {self.brand} {self.model}, nr rejestracji: {self.registration_number}, data przeglądu: {self.technical_review_date}, data ubezpieczenia: {self.insurance_date}"
