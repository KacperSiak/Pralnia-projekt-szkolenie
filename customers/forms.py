from django import forms
from django.core.exceptions import ValidationError

from customers.models import Customer


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = {"name", "address", "contact_number", "nip", "contact_person"}

    def clean_contact_number(self):
        contact_number = self.data["contact_number"]
        if not contact_number.isdigit():
            raise forms.ValidationError("Telefon musi zawierać tylko cyfry!")
        if len(contact_number) != 9:
            raise forms.ValidationError("Telefon musi zawierać 9 cyfr!")
        return contact_number

    def clean_nip(self):
        nip = self.cleaned_data['nip']
        if not nip.isdigit():
            raise ValidationError("NIP musi składać się tylko z cyfr!")
        if len(nip) != 10:
            raise forms.ValidationError("Telefon musi zawierać 10 cyfr!")

        digits =[int(number) for number in nip]
        weight = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        check_sum = sum(digit * weight for digit, weight in zip(digits, weight)) % 11
        if check_sum != digits[-1]:
            raise ValidationError("NIP się nie zgadza!")
        return nip