from django.db import models
from django.utils import timezone
from account.models import StudentProfile
from department.models import CourseOffering

class Quiz(models.Model):
    name = models.CharField(max_length=256)
    start_time = models.DateTimeField()
    description = models.TextField()
    # course_offerings = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(
        default=180, help_text='Duration in minutes')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'quizes'
    
    def __str__(self):
        return self.name

    @property
    def end_time(self):
        return self.start_time + timezone.timedelta(minutes=self.duration)

    @property
    def is_active(self):
        now = timezone.now()
        return now > self.start_time and now < self.end_time

    @property
    def total_marks(self):
        return self.question_set.aggregate(total_marks=models.Sum('positive_marks'))['total_marks']


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    correct_choice = models.ForeignKey('Choice', related_name='correct_choice_for_question', on_delete=models.CASCADE, blank=True, null=True)
    positive_marks = models.IntegerField(default=1)
    negative_marks = models.FloatField(default=-0.25)

    def __str__(self):
        return 'Q. for {}'.format(self.quiz.name)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=512)

    class Meta:
        ordering = ('text',)
    
    def __str__(self):
        return self.text


class QuizSession(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student_profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    selected_choices = models.ManyToManyField(Choice, through='ChoiceMapping', through_fields=('quiz_session', 'choice'))

    @property
    def marks_obtained(self):
        return 0


class ChoiceMapping(models.Model):
    quiz_session = models.ForeignKey(QuizSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)