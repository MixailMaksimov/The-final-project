from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_number = models.IntegerField(primary_key=True, verbose_name='Номер комнаты')
    floor = models.IntegerField(verbose_name='Этаж')
    capacity = models.IntegerField(verbose_name='Вместимость комнаты')

    def __str__(self):
        return f'Комната №{self.room_number}'

    def get_students(self):
        return ", ".join([f"{student.student_profile.id} {student.student_profile.first_name} {student.student_profile.last_name}" for student in self.students.all()])


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', verbose_name='Пользователь')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='students', verbose_name='Комната')
    course = models.IntegerField(verbose_name='Курс обучения')
    major = models.CharField(max_length=200, verbose_name='Направление обучения')

    def __str__(self):
        return f'{self.user.username} ({self.user.first_name} {self.user.last_name})'
