from django.db import models
from django.core.validators import RegexValidator
from account.models import InstructorProfile, StudentProfile
from django.contrib.auth.models import User

FILE_TYPE=(('img','Image File'),
('vid','Video File(.mp4)'),
('pdf','PDF File'),
('doc','Document Word File'),
('oth','Other')
)

class Department(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    COURSE_REGEX = RegexValidator(
        r'^[A-Z]{2}[\d]{3}$', message='not a valid course id')
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=5, validators=[COURSE_REGEX])
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CourseOffering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE)
    enrolled_students = models.ManyToManyField(StudentProfile)

    def __str__(self):
        return '{} offered by {}'.format(self.course.code, self.instructor.name)

class File(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=3,choices=FILE_TYPE,default='pdf')
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

