from django.contrib import admin
from .models import Room, Student


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'floor', 'capacity', 'get_students')

    def get_students(self, obj):
        return ", ".join([f"{student.user.username} ({student.user.first_name} {student.user.last_name})" for student in obj.students.all()])
    get_students.short_description = 'Студенты'


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'course', 'major')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('user')  # Оптимизируем запрос, чтобы избежать N+1 проблемы
        return queryset

    def user(self, obj):
        return obj.user.username

    def room(self, obj):
        return obj.room.room_number if obj.room else None


admin.site.register(Room, RoomAdmin)
admin.site.register(Student, StudentAdmin)