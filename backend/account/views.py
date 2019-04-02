from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.settings import api_settings
from account.metadata import ProfileMetadata
from account.serializers import StudentProfileSerializer, InstructorProfileSerializer


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
