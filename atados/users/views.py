from django.shortcuts import render

from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
