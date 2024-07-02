from django.contrib import admin
from .models import RepairRequest

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
