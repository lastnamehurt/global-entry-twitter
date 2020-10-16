from django import forms
from phonenumber_field.formfields import PhoneNumberField


class SignupForm(forms.Form):
    phone_number = PhoneNumberField()
