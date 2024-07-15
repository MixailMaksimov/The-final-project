from django.contrib import admin
from .models import RepairRequest, BookingCoworking


def not_booked(modeladmin, request, queryset):
    queryset.update(is_booked=False)


# Класс администратора для модели RepairRequest
@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'student_name', 'room_number', 'status', 'created_at', 'updated_at')
    list_filter = ('title', 'status', 'room_number', 'priority')
    search_fields = ('title', 'description', 'priority')
    fieldsets = (
        (None, {
            'fields': ('title', 'student_name', 'room_number', 'description')
        }),
        ('Availability', {
            'fields': ('status','priority')
        }),
    )


@admin.register(BookingCoworking)
class BookingCoworkingAdmin(admin.ModelAdmin):
    list_display = ('desk_type', 'is_booked', 'desk_number', 'student_name','booking_date', 'booking_start_time', 'booking_end_time', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('is_booked', 'desk_number', 'booking_date', 'booking_start_time', 'booking_end_time', 'student_name')
        }),
        ('Availability', {
            'fields': ('desk_type',)
        }),
    )
    actions = [not_booked]