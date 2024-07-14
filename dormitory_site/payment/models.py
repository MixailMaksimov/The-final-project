from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.OneToOneField('Room', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    due_date = models.DateField()

    def __str__(self):
        return self.user.username


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        return self.room_number


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Подтверждена'),
        ('processing', 'Обрабатывается'),
        ('rejected', 'Отклонена'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Transaction {self.id} - {self.user.user.username}'
