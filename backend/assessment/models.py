from django.db import models
from datetime import timedelta, datetime


class Quiz(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=256)
    start_time = models.DateTimeField()
    duration = models.PositiveIntegerField(
        default=180, help_text='Duration in minutes')
    is_active = models.BooleanField(default=False)

    @property
    def end_time(self):
        return self.start_time + timedelta(minutes=self.duration)
