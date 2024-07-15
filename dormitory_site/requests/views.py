from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import RepairRequest, BookingCoworking
from django.template.loader import render_to_string
from .forms import RepairRequestForm, BookingCoworkingForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from personal_account.models import Student


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'requests/index.html')


@login_required
def repair_requests_list(request):
    repair_requests = RepairRequest.objects.all()
    return render(request, 'requests/repair_requests_list.html', {'repair_requests_list': repair_requests})


@login_required
def booking_coworking_list(request):
    booking_coworking = BookingCoworking.objects.all()
    return render(request, 'requests/booking_coworking_list.html', {'booking_coworking_list': booking_coworking})


class RepairRequestDetailView(DetailView):
    model = RepairRequest
    pk_url_kwarg = 'repair_request_id'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        repair_request = self.get_object()
        return render(request, 'requests/repair_request_detail.html',{'repair_request':repair_request})

class BookingCoworkingDetailView(DetailView):
    model = BookingCoworking
    pk_url_kwarg = 'desk_number'
    template_name = 'requests/booking_coworking_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_coworking'] = self.get_object()
        return context

class RepairRequestCreateView(LoginRequiredMixin, CreateView):
    model = RepairRequest
    form_class = RepairRequestForm
    template_name = 'requests/repair_request_form.html'
    success_url = reverse_lazy('requests:repair_requests_list')
    def form_valid(self, form):
        user = self.request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:
            form.add_error(None, "Студент не найден.")
            return self.form_invalid(form)
        
        form.instance.user = user
        form.instance.room = student.room
        return super().form_valid(form)


class BookingCoworkingCreateView(CreateView):
    model = BookingCoworking
    form_class = BookingCoworkingForm
    template_name = 'requests/booking_coworking_form.html'
    success_url = reverse_lazy('requests:booking_coworking_list')

class RepairRequestUpdateView(UpdateView):
    model = RepairRequest
    pk_url_kwarg = 'repair_request_id'
    form_class = RepairRequestForm
    template_name = 'requests/repair_request_update.html'
    success_url = reverse_lazy('requests:repair_requests_list')

class BookingCoworkingUpdateView(UpdateView):
    model = BookingCoworking
    pk_url_kwarg = 'desk_number'
    form_class = BookingCoworkingForm
    template_name = 'requests/booking_coworking_update.html'
    success_url = reverse_lazy('requests:booking_coworking_list')


@login_required
def select_free_desk(request, preference):
    if request.method == 'POST':
        form = BookingCoworkingForm(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['booking_date']
            booking_start_time = form.cleaned_data['booking_start_time']
            booking_end_time = form.cleaned_data['booking_end_time']

            if preference == 'Any':
                desk = BookingCoworking.objects.filter(is_booked=False).first()
            else:
                desk = BookingCoworking.objects.filter(desk_type=preference, is_booked=False).first()
            if desk:
                desk.booking_date = booking_date
                desk.booking_start_time = booking_start_time
                desk.booking_end_time = booking_end_time
                user = request.user
                desk.user = user
                desk.is_booked = True
                desk.save()
                return redirect(reverse('requests:booking_coworking_list'))
            else:
                return render(request, 'requests:no_items_available.html')
    else:
        form = BookingCoworkingForm()
    return render(request, 'requests/select_free_desk.html', {'form': form})   


@login_required
def clear_booking(request, desk_number):
    booking_coworking = get_object_or_404(BookingCoworking, desk_number=desk_number)
    booking_coworking.booking_date = None
    booking_coworking.booking_start_time = None
    booking_coworking.booking_end_time = None
    booking_coworking.is_booked = False
    booking_coworking.user = None
    booking_coworking.save()
    booking_coworking = BookingCoworking.objects.all()
    return render(request, 'requests/booking_coworking_list.html', {'booking_coworking_list': booking_coworking})

class RepairRequestDeleteView(View):
    success_url = reverse_lazy('requests:repair_requests_list')

    def post(self, request, *args, **kwargs):
        repair_request_id = kwargs['repair_request_id']
        repair_request = RepairRequest.objects.get(id=repair_request_id)
        repair_request.delete()
        return HttpResponseRedirect(self.success_url)

class BookingCoworkingDeleteView(View):
    success_url = reverse_lazy('requests:booking_coworking_list')

    def post(self, request, *args, **kwargs):
        desk_number = kwargs['desk_number']
        booking_coworking = BookingCoworking.objects.get(desk_number=desk_number)
        booking_coworking.delete()
        return HttpResponseRedirect(self.success_url)