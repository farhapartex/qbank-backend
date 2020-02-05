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


class DepartmentAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer