from django.contrib import admin
from .models import RepairRequest, BookingCoworking


def not_booked(modeladmin, request, queryset):
    queryset.update(is_booked=False)
    queryset.update(booking_date=None)
    queryset.update(booking_start_time=None)
    queryset.update(booking_end_time=None)
    queryset.update(user=None)

# Класс администратора для модели RepairRequest
@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'user', 'room', 'status', 'created_at', 'updated_at')
    list_filter = ('title', 'status', 'priority')
    search_fields = ('title', 'description', 'priority')
    fieldsets = (
        (None, {
            'fields': ('title',  'description')
        }),
        ('Availability', {
            'fields': ('status','priority','user')
        }),
    )


@admin.register(BookingCoworking)
class BookingCoworkingAdmin(admin.ModelAdmin):
    list_display = ('desk_type', 'is_booked', 'desk_number', 'user','booking_date', 'booking_start_time', 'booking_end_time', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('is_booked', 'desk_number', 'booking_date', 'booking_start_time', 'booking_end_time')
        }),
        ('Availability', {
            'fields': ('desk_type',)
        }),
    )
    actions = [not_booked]