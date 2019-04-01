from django.db import models
from django.utils import timezone


class Quiz(models.Model):
    name = models.CharField(max_length=256)
    start_time = models.DateTimeField()
    duration = models.PositiveIntegerField(
        default=180, help_text='Duration in minutes')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'quizes'

    @property
    def end_time(self):
        return self.start_time + timezone.timedelta(minutes=self.duration)

    @property
    def is_active(self):
        now = timezone.now()
        return now > self.start_time and now < self.end_time
