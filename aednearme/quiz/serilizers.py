from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = (
            'id', 
            'quiz_subject',
            'question_1', 
            'question_2', 
            'question_3',
            'question_4',
            'question_5',
            'question_6',
            'correct_answer_1',
            'correct_answer_2', 
            'correct_answer_3',
            'correct_answer_4',
            'correct_answer_5',
            'correct_answer_6',
            'incorrect_answers_1',
            'incorrect_answers_2',
            'incorrect_answers_3',
            'incorrect_answers_4',
            'incorrect_answers_5',
            'incorrect_answers_6' 
        )