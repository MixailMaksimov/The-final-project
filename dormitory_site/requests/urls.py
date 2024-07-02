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
]