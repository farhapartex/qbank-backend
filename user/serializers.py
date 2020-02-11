import logging
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *


logger = logging.getLogger(__name__)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class MinimalDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("id","name")

class UserMinimalSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, model):
        if model.first_name or model.last_name:
            return " ".join(
                list(
                    filter(
                        lambda x: x is not None or bool(x),
                        [model.first_name, model.last_name],
                    )
                )
            ).strip()
        else:
            return model.username

    class Meta:
        model = User
        fields = ("id","username","full_name","email")


class FlatUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, model):
        if model.first_name or model.last_name:
            return " ".join(
                list(
                    filter(
                        lambda x: x is not None or bool(x),
                        [model.first_name, model.last_name],
                    )
                )
            ).strip()
        else:
            return model.username
    class Meta:
        model = User
        fields = ("id","first_name","last_name","username","full_name","email","last_login")


class ProfileSerializer(serializers.ModelSerializer):
    department = MinimalDepartmentSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ("id","department","session")


class UserSerializer(serializers.ModelSerializer):
    uprofile = ProfileSerializer()

    class Meta:
        model = User
        fields = ("id","first_name","last_name","email","username","image","last_login","groups","uprofile")
        read_only_fields = ('user_permissions',)
        
class RegistrationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","username","email","password")


