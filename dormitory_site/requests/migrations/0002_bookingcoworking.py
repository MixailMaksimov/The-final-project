# Generated by Django 5.0.6 on 2024-07-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingCoworking',
            fields=[
                ('desk_number', models.IntegerField(primary_key=True, serialize=False)),
                ('desk_type', models.CharField(choices=[('With_Computer', 'С компьютером'), ('Without_Computer', 'Без компьютера'), ('Any', 'Любой')], max_length=20)),
                ('is_booked', models.BooleanField(default=False)),
                ('student_name', models.CharField(max_length=100)),
                ('booking_date', models.DateField(blank=True, null=True, verbose_name='Дата бронирования')),
                ('booking_start_time', models.TimeField(blank=True, null=True, verbose_name='Время начала бронирования')),
                ('booking_end_time', models.TimeField(blank=True, null=True, verbose_name='Время окончания бронирования')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
