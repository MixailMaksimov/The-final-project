from django.urls import path, include
from requests import views

app_name = 'requests'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    path('repair_requests/', views.repair_requests_list, name='repair_requests_list'), 
    path('repair_requests/<int:repair_request_id>/', views.RepairRequestDetailView.as_view(), name='repair_request_detail'),
    path('repair_requests/create_repair_request/', views.RepairRequestCreateView.as_view(), name='create_repair_request'),
    path('repair_requests/<int:repair_request_id>/update_repair_request/', views.RepairRequestUpdateView.as_view(), name='update_repair_request'),
    path('repair_requests/<int:repair_request_id>/delete_repair_request/', views.RepairRequestDeleteView.as_view(), name='delete_repair_request'),
    
    path('booking_coworking/', views.booking_coworking_list, name='booking_coworking_list'), 
    path('booking_coworking/<int:desk_number>/', views.BookingCoworkingDetailView.as_view(), name='booking_coworking_detail'),
    path('booking_coworking/create_booking_coworking/', views.BookingCoworkingCreateView.as_view(), name='create_booking_coworking'),
    path('booking_coworking/<int:desk_number>/update_booking_coworking/', views.BookingCoworkingUpdateView.as_view(), name='update_booking_coworking'),
    path('booking_coworking/<int:desk_number>/delete_booking_coworking/', views.BookingCoworkingDeleteView.as_view(), name='delete_booking_coworking'),
    path('booking_coworking/clear_booking/<int:desk_number>/', views.clear_booking, name='clear_booking'),
    path('booking_coworking/select_free_desk/<str:preference>/', views.select_free_desk, name='select_free_desk'),

]