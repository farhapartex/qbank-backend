import logging
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


logger = logging.getLogger(__name__)

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


class RegistrationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","username","email","password")
