from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from department.models import Department, Course, CourseOffering, FileModel
from department.permissions import IsStudent, IsInstructor
from account.models import StudentProfile, InstructorProfile


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'name')


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Course
        fields = ('name', 'code', 'department')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileModel
        fields = ('name', 'file_type', 'file_data', 'course_offering')


class enrolledStrudentSerializer(serializers.HyperlinkedModelSerializer):
    department = DepartmentSerializer()
    user = UserSerializer()

    class Meta:
        model = StudentProfile
        fields = ('user', 'roll_number', 'department')


class CourseInstructorSerializer(serializers.HyperlinkedModelSerializer):
    department = DepartmentSerializer()
    user = UserSerializer()

    class Meta:
        model = InstructorProfile
        fields = ('user', 'department')


class CourseOfferingSerializer(serializers.HyperlinkedModelSerializer):
    enrolled_students = enrolledStrudentSerializer(many=True)
    instructor = CourseInstructorSerializer()
    course = CourseSerializer()

    class Meta:
        model = CourseOffering
        fields = ('course', 'instructor', 'enrolled_students')


class FileVIewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer


class CourseOfferingViewSet(viewsets.ModelViewSet):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer

    def get_permissions(self):
        if self.action in ['enroll']:
            self.permission_classes = (IsStudent,)
        elif self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = (AllowAny,)
        return super().get_permissions()

    @action(methods=['get'], detail=True)
    def enroll(self, request, pk=None):
        get_object_or_404(CourseOffering, pk=pk).enrolled_students.add(
            request.user.studentprofile)
        return Response(data={'message': 'enrolled'}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def offer_course(self, request, pk=None):
        get_object_or_404(CourseOffering, pk=pk).enrolled_students.add(
            request.user.studentprofile)
        return Response(data={'message': 'enrolled'}, status=status.HTTP_200_OK)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
