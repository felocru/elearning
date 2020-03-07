from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from core.models import Course, Question, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AnswerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = AnswerSerializer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
    expandable_fields = {
        'answers': (AnswerSerializer, {'many':True})
    }

class LessonSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
    expandable_fields = {
        'question_set': (QuestionSerializer, {'many':True})
    }



