from django import forms
from django.forms import ModelForm
from .models import RepairRequest

class RepairRequestForm(ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['title', 'description', 'student_name', 'room_number', 'status', 'priority']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'student_name': 'Имя студента',
            'room_number': 'Номер комнаты',
            'status': 'Статус',
            'priority': 'Приоритет',
        }