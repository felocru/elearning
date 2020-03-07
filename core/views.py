from django.shortcuts import render
from rest_framework import serializers, viewsets
from core.models import Course, Lesson, Question
from core.serializers import CourseSerializer, LessonSerializer, QuestionSerializer
from core.filters import CourseFilterBackend, LessonFilterBackend
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [CourseFilterBackend]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [LessonFilterBackend]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
