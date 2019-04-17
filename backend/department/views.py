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
from department.models import File

# Create your views here.


class FileUploadAPIView(APIView):
    http_method_names = ['post','put']
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        instance = File(file=request.FILES['file'],name=request.data['name'])
        instance.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, format= None):
        file_instance = File.objects.get(file=request.FILES['file'])
        file_instance.delete(save=True)
    