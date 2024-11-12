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


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        language = self.request.query_params.get('language')
        difficulty = self.request.query_params.get('difficulty')
        if language:
            queryset = queryset.filter(language__name=language)
        if difficulty:
            queryset = queryset.filter(difficulty__level=difficulty)
        return queryset