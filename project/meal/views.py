from django.shortcuts import render

# Create your views here.

#viewset
from rest_framework import viewsets
from .serializers import MealRateSerializer
from .models import MealRate

class MealRateViewSet(viewsets.ModelViewSet):
    queryset = MealRate.objects.all()
    serializer_class = MealRateSerializer