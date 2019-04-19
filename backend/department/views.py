from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from department.permissions import IsStudent, IsInstructor
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.settings import api_settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from department.models import FileModel
from rest_framework import generics
from department.serializers import FileSerializer
# Create your views here.

class FileList(generics.ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        code = self.request.query_params.get('code')
        print(code)
        return FileModel.objects.filter(course_offering__course__code=code)
