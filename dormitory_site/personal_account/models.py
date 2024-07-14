from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_number = models.IntegerField(primary_key=True, verbose_name='Номер комнаты')
    floor = models.IntegerField(verbose_name='Этаж')
    capacity = models.IntegerField(verbose_name='Вместимость комнаты')

    def __str__(self):
        return f'Комната №{self.room_number}'

    def get_students(self):
        return ", ".join([f"{student.id} {student.first_name} {student.last_name}" for student in self.students.all()])


class Student(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='students', verbose_name='Комната')
    course = models.IntegerField(verbose_name='Курс обучения')
    major = models.CharField(max_length=200, verbose_name='Направление обучения')
    login = models.CharField(max_length=100, verbose_name='Логин')
    password = models.CharField(max_length=100, verbose_name='Пароль')

    def save(self, *args, **kwargs):
        if not self.login:
            self.login = f'User{self.id}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.last_name} {self.first_name} {self.middle_name}'
