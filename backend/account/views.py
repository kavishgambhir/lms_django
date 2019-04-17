from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.settings import api_settings
from account.metadata import ProfileMetadata
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from account.serializers import StudentProfileSerializer, InstructorProfileSerializer
from account.models import StudentProfile, InstructorProfile


class ProfileCreateAPIView(APIView):
    http_method_names = ['head', 'options', 'post']
    permission_classes = (AllowAny,)
    serializer_class = None
    metadata_class = ProfileMetadata
    serializer_mapper = {
        'student': StudentProfileSerializer,
        'instructor': InstructorProfileSerializer
    }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def create(self, data):
        try:
            profile_type = data['type']
            self.serializer_class = self.serializer_mapper[profile_type]
        except (MultiValueDictKeyError, KeyError):
            return Response({
                'type': ['This field is required']
            }, status=status.HTTP_400_BAD_REQUEST)
        data = dict(data)
        data.pop('type')
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def post(self, request, *args, **kwargs):
        return self.create(request.data)


class LoginAPIView(APIView):
    http_method_names = ['get', 'post', 'options', 'head']
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"data": self.get_profile_data(request, request.user) or "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": ["you must authorize via POST request first"]}, status=status.HTTP_401_UNAUTHORIZED)

    # @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        user = authenticate(request=request, username=request.data.get(
            'username', ''), password=request.data.get('password', ''))
        if user:
            auth_login(request, user)
            return Response({"data": self.get_profile_data(request, user) or "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": ["invalid credentials"]}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_profile_data(request, user):
        try:
            instructor_profile = InstructorProfile.objects.get(user=user)
            return {'type': 'instructor-profile', 'profile': InstructorProfileSerializer(instance=instructor_profile, context={'request': request}).data}
        except InstructorProfile.DoesNotExist:
            try:
                student_profile = StudentProfile.objects.get(user=user)
                return {'type': 'student-profile', 'profile': StudentProfileSerializer(instance=student_profile, context={'request': request}).data}
            except StudentProfile.DoesNotExist:
                return {}


class LogoutAPIView(APIView):
    http_method_names = ['get', 'options', 'head']
    permission_classes = (AllowAny,)

    @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            auth_logout(request)
            return Response({"message": "user logged out"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "no User is logged in"}, status=status.HTTP_304_NOT_MODIFIED)


class AuthenticationCheckAPIView(APIView):
    permission_classes = (AllowAny,)
    """
        get:
        Returns the authentication status code and message for current request.
    """

    def get(self, request, *args, **kwargs):
        authenticated = request.user.is_authenticated
        data = {
            'message': 'Authorized' if authenticated else 'Unauthorized'
        }
        status_code = status.HTTP_200_OK if authenticated else status.HTTP_401_UNAUTHORIZED
        return Response(data, status=status_code)
