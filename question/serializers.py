import logging
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


logger = logging.getLogger(__name__)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"