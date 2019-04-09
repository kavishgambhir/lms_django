from django.contrib import admin
from assessment.models import Quiz, Question, Choice, ChoiceMapping, QuizSession


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ChoiceMapping)
admin.site.register(QuizSession)