from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9) # walidacja
    contact_person = models.CharField(max_length=100)
    nip = models.CharField(max_length=11)
    contract_number = models.ForeignKey("Contracts",related_name="contract_number", on_delete=models.CASCADE)

    def __str__(self):
        return f"Customer: {self.name}"


class Contract(models.Model):
    number = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_leased = models.BooleanField(default=False)
    name_of_stock = models.CharField(max_length=100)
    price_for_kg = models.FloatField()
    payment_date = models.DateField()
    delivered_by_car_number = models.ForeignKey("Cars",related_name="registration_number", on_delete=models.CASCADE)

    def __str__(self):
        return f"Contract: {self.number}"


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=8)
    technical_review_date = models.DateField()
    insurance_date = models.DateField()

    def __str__(self):
        return f"Car: {self.brand} - {self.model}"


class Stock(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_weight = models.FloatField()

    def __str__(self):
        return f"Stock: {self.name}"

