from django.shortcuts import render
from .serializers import *
from .models import Action
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class ActionViewSet(ModelViewSet):
    serializer_class = ActionSerializer
    queryset = Action.objects.all()

