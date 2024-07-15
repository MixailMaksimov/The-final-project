from django import forms
from .models import GuestRequest


class GuestRequestForm(forms.ModelForm):
    class Meta:
        model = GuestRequest
        fields = ['guest_name', 'guest_passport', 'guest_arrival', 'guest_departure']