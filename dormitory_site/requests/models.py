from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from personal_account.models import Room, Student

# Create your models here.
class RepairRequest(models.Model):

    STATUS_CHOICES = [
        ('New', 'Новый'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершен'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Высокий'),
        (2, 'Средний'),
        (3, 'Низкий'),
    ]

    def __str__(self):
        return self.title

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=100)
    description = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, verbose_name='Комната')
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=2,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookingCoworking(models.Model):
    TYPE_CHOICES = [
        ('With_Computer', 'С компьютером'),
        ('Without_Computer', 'Без компьютера'),
        ('Any', 'Любой'),
    ]
    
    desk_number = models.IntegerField(primary_key=True)
    desk_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    is_booked = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True, verbose_name="Дата бронирования")
    booking_start_time = models.TimeField(null=True, blank=True, verbose_name="Время начала бронирования")
    booking_end_time = models.TimeField(null=True, blank=True, verbose_name="Время окончания бронирования")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
