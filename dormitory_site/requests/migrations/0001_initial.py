# Generated by Django 5.0.7 on 2024-07-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingCoworking',
            fields=[
                ('desk_number', models.IntegerField(primary_key=True, serialize=False)),
                ('desk_type', models.CharField(choices=[('With_Computer', 'С компьютером'), ('Without_Computer', 'Без компьютера'), ('Any', 'Любой')], max_length=20)),
                ('is_booked', models.BooleanField(default=False)),
                ('student_name', models.CharField(blank=True, max_length=100, null=True)),
                ('booking_date', models.DateField(blank=True, null=True, verbose_name='Дата бронирования')),
                ('booking_start_time', models.TimeField(blank=True, null=True, verbose_name='Время начала бронирования')),
                ('booking_end_time', models.TimeField(blank=True, null=True, verbose_name='Время окончания бронирования')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepairRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('student_name', models.CharField(max_length=100)),
                ('room_number', models.IntegerField()),
                ('status', models.CharField(choices=[('New', 'Новый'), ('In_progress', 'В работе'), ('Completed', 'Завершен')], default='New', max_length=50)),
                ('priority', models.IntegerField(choices=[(1, 'Высокий'), (2, 'Средний'), (3, 'Низкий')], default=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]