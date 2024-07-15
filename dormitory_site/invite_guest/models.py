from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .validators import validate_name, validate_passport_number


class GuestRequest(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    user_id = models.ForeignKey(null=True, on_delete=models.SET_NULL, to='personal_account.student', verbose_name='Студент')    
    guest_name = models.CharField(max_length=100, validators = [validate_name])
    guest_passport = models.IntegerField(validators = [validate_passport_number])
    guest_arrival = models.DateTimeField()
    guest_departure = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f'{self.guest_name} в гостях у {self.user.username}'
