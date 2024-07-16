from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import GuestRequestForm
from .models import GuestRequest, Student
from django.utils import timezone
from django.core.mail import send_mail

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'invite_guest/index.html')

@login_required
def guest_request_view(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        form = GuestRequestForm(request.POST)
        if form.is_valid():
            guest_request = form.save(commit=False)
            guest_request.user = student  # Используем экземпляр Student
            guest_request.save()
            return redirect('guests:guest_list_view')
    else:
        form = GuestRequestForm()

    current_guests = GuestRequest.objects.filter(user=student, guest_departure__isnull=True)
    return render(request, 'invite_guest/guest_request.html', {'form': form, 'current_guests': current_guests})

@login_required
def guest_list_view(request):
    student = get_object_or_404(Student, user=request.user)
    current_guests = GuestRequest.objects.filter(user=student, guest_departure__isnull=True)
    return render(request, 'invite_guest/guest_list.html', {'current_guests': current_guests})

def send_guest_notification():
    current_guests = GuestRequest.objects.filter(guest_departure__isnull=True)
    for guest in current_guests:
        if guest.guest_arrival.date() == timezone.now().date() and timezone.now().hour == 23:
            send_mail(
                'Guest Notification',
                'Выгоняйте гостя!',
                'admin@example.com',
                [guest.user.user.email],  # Изменено на guest.user.user.email
                fail_silently=False,
            )

@login_required
def repeat_guest_request_view(request, guest_id):
    student = get_object_or_404(Student, user=request.user)
    guest_request = get_object_or_404(GuestRequest, id=guest_id, user=student)
    guest_request.pk = None  # Сброс идентификатора для создания новой записи
    guest_request.guest_arrival = timezone.now()
    guest_request.guest_departure = None
    guest_request.save()
    return redirect('guests:guest_list_view')