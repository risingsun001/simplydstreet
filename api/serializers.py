from django.shortcuts import get_object_or_404

# import serializer from rest_framework
from rest_framework import serializers
from rest_framework.fields import empty

# import model from models.py
from .models import *

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = "__all__"

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = "__all__"