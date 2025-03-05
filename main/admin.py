from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "rollno", "email", "phone", "otp")
    search_fields = ("name", "rollno", "email")
