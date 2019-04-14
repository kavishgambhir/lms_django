from rest_framework import serializers, viewsets
from department.models import Department, Course, CourseOffering


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


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
