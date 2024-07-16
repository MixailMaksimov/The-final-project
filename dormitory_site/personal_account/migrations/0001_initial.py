# Generated by Django 5.0.7 on 2024-07-14 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер комнаты')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('capacity', models.IntegerField(verbose_name='Вместимость комнаты')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('course', models.IntegerField(verbose_name='Курс обучения')),
                ('major', models.CharField(max_length=200, verbose_name='Направление обучения')),
                ('login', models.CharField(max_length=100, verbose_name='Логин')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='personal_account.room', verbose_name='Комната')),
            ],
        ),
    ]
