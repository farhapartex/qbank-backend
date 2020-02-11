import logging
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from user.serializers import DepartmentSerializer, MinimalDepartmentSerializer


logger = logging.getLogger(__name__)

class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    class Meta:
        model = Course
        fields = "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    department = MinimalDepartmentSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ("id","code","name",'department')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionDetailSerializer(serializers.ModelSerializer):
    department = MinimalDepartmentSerializer(read_only=True)
    course = MinimalCourseSerializer(read_only=True)

    class Meta:
        model = Question
        fields = "__all__"