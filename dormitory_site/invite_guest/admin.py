from django.contrib import admin
from .models import GuestRequest


@admin.register(GuestRequest)
class GuestRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'guest_name', 'guest_passport', 'guest_arrival', 'guest_departure', 'created_at']
    list_filter = ['user_id', 'guest_arrival', 'created_at']
    search_fields = ['guest_name', 'guest_passport']
    date_hierarchy = 'guest_arrival'
    ordering = ['-guest_arrival']
