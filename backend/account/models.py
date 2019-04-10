from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=10, unique=True)
    dob = models.DateField()
    avatar = models.ImageField(upload_to='avatar',null=True)
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    def __str__(self):
        return '{} ({})'.format(self.name, self.roll_number)

    @property
    def name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)

    @property
    def name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    