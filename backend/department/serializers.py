from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from department.models import Department, Course, CourseOffering
from department.permissions import IsStudent, IsInstructor
from account.models import StudentProfile


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'name')


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CourseOfferingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseOffering
        fields = ('course', 'instructor', 'enrolled_students')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'code', 'department')


class CourseOfferingViewSet(viewsets.ModelViewSet):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer

    def get_permissions(self):
        if self.action in ['enroll']:
            self.permission_classes = (IsStudent,)
        elif self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = (IsInstructor,)
        return super().get_permissions()

    @action(methods=['get'], detail=True)
    def enroll(self, request, pk=None):
        get_object_or_404(CourseOffering, pk=pk).enrolled_students.add(request.user.studentprofile)
        return Response(data={'message': 'enrolled'}, status=status.HTTP_200_OK)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
