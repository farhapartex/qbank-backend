import logging
from django.shortcuts import render, get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters as drf_filters
from .models import *
from .serializers import *

logger = logging.getLogger(__name__)

"""
FILTERS
"""

class CourseFilter(filters.FilterSet):
    id = filters.CharFilter(method="filter_by_department_id")

    def filter_by_department_id(self, queryset, name, value):
        if value is None:
            return queryset
        try:
            return queryset.filter(department__id=value)
        except:
            return []

    class Meta:
        model = Course
        fields = ("id",)


"""
API Views
"""

class DepartmentAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CourseAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter

class QuestionAPIViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)