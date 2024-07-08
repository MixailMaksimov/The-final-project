from django.urls import path
from . import views

app_name = 'guests'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('guests/', views.guest_list_view, name='guest_list_view'),
    path('guest/request/', views.guest_request_view, name='guest_request_view'),
    path('guest/repeat_request/<int:guest_id>/', views.repeat_guest_request_view, name='repeat_guest_request_view')
]