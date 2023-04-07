from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.db.models import Value, TextField
from django.db.models.functions import Concat
# Create your views here.

from functools import reduce

from .permissions import IsAdminOrReadOnly
from .models import *
from .serializers import *

class ExchangeViewSet(ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    pagination_class = None
    permission_classes = [IsAdminOrReadOnly]

class SecurityViewSet(ModelViewSet):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        mic = self.request.GET.get('mic', '')
        queryset = self.queryset if mic=='' else self.queryset.filter(mic=mic)
        
        search_word = self.request.GET.get('search', '').lower()
        if search_word:
            queryset = queryset.annotate(text=Concat('symbol', Value(' '), 'name', output_field=TextField()))
            queryset = queryset.filter(text__icontains=search_word)
        
        return queryset