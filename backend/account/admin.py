from django.contrib import admin
from account.models import StudentProfile, InstructorProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'roll_number')
    search_fields = ('roll_number',)

@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    pass