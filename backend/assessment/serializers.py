from rest_framework import serializers, viewsets
from assessment.models import Quiz


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('url', 'name', 'start_time', 'duration', 'end_time', 'is_active', 'uploaded_at')
        read_only_fields = ('end_time', 'is_active')


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer