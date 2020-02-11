import logging
from django.shortcuts import render, get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters as drf_filters
from rest_framework.response import Response
from rest_framework.request import Request
from .models import *
from .serializers import *

logger = logging.getLogger(__name__)


class RegistrationAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationUserSerializer

class CheckUserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = FlatUserSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        return User.objects.filter(username=username)


class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request:Request, *args, **kwargs):
        logger.critical(kwargs.get('pk'))
        if kwargs.get('pk') == 'me':
            return Response(self.get_serializer(request.user).data)
        user = get_object_or_404(User.objects.all(), pk = kwargs.get('pk'))

        return Response(UserSerializer(user).data)

    def get_serializer_class(self):
        return FlatUserSerializer if self.action == "list" else UserSerializer