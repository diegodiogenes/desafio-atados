from rest_framework import serializers
from .models import Action
from users.models import User


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = '__all__'

