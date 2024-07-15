'''from celery import shared_task
from django.utils import timezone
from .models import BookingCoworking

@shared_task
def clear_expired_bookings():
    now = timezone.now()
    expired_bookings = BookingCoworking.objects.filter(
        booking_end_time__lte=now.time(),
        booking_date__lte=now.date(),
        student_name__isnull=False
    )
    expired_bookings.update(student_name=None)
'''

