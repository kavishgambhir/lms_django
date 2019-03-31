from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=10)

    def __str__(self):
        return '{} ({})'.format(self.name, self.roll_number)

    @property
    def name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
