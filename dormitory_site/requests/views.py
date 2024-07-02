from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import RepairRequest
from django.template.loader import render_to_string
from .forms import RepairRequestForm
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'requests/index.html')

def repair_requests_list(request):
    repair_requests = RepairRequest.objects.all()
    return render(request, 'requests/repair_requests_list.html', {'repair_requests_list': repair_requests})

class RepairRequestDetailView(DetailView):
    model = RepairRequest
    pk_url_kwarg = 'repair_request_id'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        repair_request = self.get_object()
        return render(request, 'requests/repair_request_detail.html',{'repair_request':repair_request})

class RepairRequestCreateView(CreateView):
    model = RepairRequest
    form_class = RepairRequestForm
    template_name = 'requests/repair_request_form.html'
    success_url = reverse_lazy('requests:repair_requests_list')

class RepairRequestUpdateView(UpdateView):
    model = RepairRequest
    pk_url_kwarg = 'repair_request_id'
    form_class = RepairRequestForm
    template_name = 'requests/repair_request_update.html'
    pk_url_kwarg = 'repair_request_id'
    success_url = reverse_lazy('requests:repair_requests_list')

class RepairRequestDeleteView(View):
    success_url = reverse_lazy('requests:repair_requests_list')

    def post(self, request, *args, **kwargs):
        repair_request_id = kwargs['repair_request_id']
        repair_request = RepairRequest.objects.get(id=repair_request_id)
        repair_request.delete()
        return HttpResponseRedirect(self.success_url)