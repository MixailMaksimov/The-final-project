from django.contrib import admin
from .models import Room, Student


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'floor', 'capacity', 'get_students')
    search_fields = ('room_number', 'floor')

    def get_students(self, obj):
        return ", ".join([f"{student.first_name} {student.last_name}" for student in obj.get_students()])
    get_students.short_description = 'Студенты'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name', 'room', 'course', 'major')
    search_fields = ('id', 'last_name', 'first_name', 'middle_name', 'room__room_number', 'course', 'major')
