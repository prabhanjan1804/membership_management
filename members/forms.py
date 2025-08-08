from django import forms
from .models import Member

class RegistrationForm(forms.ModelForm):
    stusta_resident = forms.BooleanField(
        label="Ich wohne in der StuSta",
        required=False
    )

    class Meta:
        model = Member
        fields = [
            'stusta_resident',     # ← new logical field (not saved)
            'name',
            'birth_date',
            'email',
            'country_code',
            'phone',
            'application_reason',
            'dorm_room',
            'street_address',
            'postal_code_city',
        ]

        labels = {
            'name': 'Vor- und Nachname',
            'birth_date': 'Geburtsdatum',
            'email': 'E-Mail-Adresse',
            'country_code': 'Landesvorwahl',
            'phone': 'Telefonnummer',
            'application_reason': 'Grund für den Antrag',
            'dorm_room': 'Haus, Zimmernummer',
            'street_address': 'Straße, Hausnummer',
            'postal_code_city': 'PLZ, Ort',
        }

        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'placeholder': 'z. B. Max Mustermann'}),
            'email': forms.EmailInput(attrs={'placeholder': 'max@example.com'}),
            'country_code': forms.TextInput(attrs={'placeholder': '+49'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '1234567890'}),
            'application_reason': forms.Textarea(attrs={'rows': 4}),
            'dorm_room': forms.TextInput(attrs={'placeholder': 'z. B. 10.03'}),
            'street_address': forms.TextInput(attrs={'placeholder': 'z. B. Musterstraße 5'}),
            'postal_code_city': forms.TextInput(attrs={'placeholder': 'z. B. 80805 München'}),
        }

class PassiveRenewalForm(forms.Form):
    email = forms.EmailField(
        label="E-Mail-Adresse",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Bitte E-Mail-Adresse eingeben',
            'class': 'form-control'
        })
    )