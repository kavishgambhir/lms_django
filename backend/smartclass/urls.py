"""smartclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, urls
from assessment.serializers import QuizViewSet
from department.serializers import DepartmentViewSet , CourseOfferingViewSet, CourseViewSet, FileVIewSet
from department.views import FileList 
from account.serializers import StudentProfileViewSet, InstructorProfileViewSet
from account.views import ProfileCreateAPIView, LoginAPIView, LogoutAPIView, AuthenticationCheckAPIView
from django.contrib.auth.views import LoginView

router = routers.DefaultRouter()
router.register(r'quizes', QuizViewSet)
router.register(r'student-profiles', StudentProfileViewSet)
router.register(r'instructor-profiles', InstructorProfileViewSet)
router.register(r'quizes', QuizViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'courses',CourseViewSet)
router.register(r'course-offerings',CourseOfferingViewSet)
router.register(r'files',FileVIewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/sign-up/', ProfileCreateAPIView.as_view(), name='sign-up'),
    path('api/sign-in/', LoginAPIView.as_view(), name='sign-in'),
    path('api/sign-out/', LogoutAPIView.as_view(), name='sign-out'),
    path('api/auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check'),
    path('api/file-by/', FileList.as_view())
]

# url('^api/file/by/(?P<course_offering>.+)/$',FileList.as_view())


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)