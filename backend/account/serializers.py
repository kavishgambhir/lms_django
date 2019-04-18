from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from account.models import StudentProfile, InstructorProfile
from department.models import CourseOffering, Course
from department.serializers import CourseSerializer

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class StudentProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = StudentProfile
        fields = ('url', 'user', 'roll_number', 'dob', 'avatar', 'department')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return StudentProfile.objects.create(user=user, **validated_data)


class InstructorProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = InstructorProfile
        fields = ('url', 'user', 'department')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return InstructorProfile.objects.create(user=user, **validated_data)


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    @action(methods=['get'], detail=True)
    def enrolled_courses(self, request, pk=None):
        course_ids = request.user.studentprofile.courseoffering_set.values_list('course', flat=True)
        courses = Course.objects.filter(id__in=course_ids)
        return Response(data=CourseSerializer(courses, many=True, context={'request': request}).data, status=status.HTTP_200_OK)


class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer
