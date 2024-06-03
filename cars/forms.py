from django import forms
from .models import Cars

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['brand', 'model', 'registration_number', 'technical_review_date', 'insurance_date']
