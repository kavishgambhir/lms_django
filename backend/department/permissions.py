from rest_framework.permissions import BasePermission
from account.models import StudentProfile, InstructorProfile


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and StudentProfile.objects.filter(user=request.user).exists())


class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and InstructorProfile.objects.filter(user=request.user).exists())