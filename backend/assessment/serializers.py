from rest_framework import serializers, viewsets
from assessment.models import Quiz, Question, Choice
from rest_framework.permissions import AllowAny


class ChoiceSerializer(serializers.ModelSerializer):
    # is_correct = serializers.BooleanField(default=False)

    class Meta:
        model = Choice
        fields = ('id', 'text')


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('text', 'correct_choice', 'negative_marks', 'positive_marks', 'choices')


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ('url', 'name', 'start_time', 'duration', 'end_time', 'is_active', 'uploaded_at', 'description', 'questions')
        read_only_fields = ('end_time', 'is_active')
    
    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            choices_data = question_data.pop('choices')
            question = Question.objects.create(quiz=quiz, **question_data)
            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)
        return quiz


class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
