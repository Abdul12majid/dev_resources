from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Resource, Language, DifficultyLevel, Tag
from .serializers import ResourceSerializer, LanguageSerializer, DifficultyLevelSerializer, TagSerializer

# Create your views here.


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class DifficultyLevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DifficultyLevel.objects.all()
    serializer_class = DifficultyLevelSerializer
