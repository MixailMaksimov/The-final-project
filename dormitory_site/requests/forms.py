from django import forms
from django.forms import ModelForm
from .models import RepairRequest, BookingCoworking
class RepairRequestForm(ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['title', 'description', 'priority']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'priority': 'Приоритет'
        }



class BookingCoworkingForm(forms.ModelForm):
    class Meta:
        model = BookingCoworking
        fields = ['booking_date', 'booking_start_time', 'booking_end_time']
        labels = {
            'desk_type': 'Тип стола',
        }
