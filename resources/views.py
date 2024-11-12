from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Resource, Language, DifficultyLevel, Tag
from .serializers import ResourceSerializer, LanguageSerializer, DifficultyLevelSerializer, TagSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


@api_view(['POST'])
def create_resource(request):
    serializer = ResourceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_resource(request, resource_id):
    try:
        resource = Resource.objects.get(id=resource_id)
    except Resource.DoesNotExist:
        return Response({"error": "Resource not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ResourceSerializer(resource, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_resource(request, resource_id):
    try:
        resource = Resource.objects.get(id=resource_id)
    except Resource.DoesNotExist:
        return Response({"error": "Resource not found."}, status=status.HTTP_404_NOT_FOUND)

    resource.delete()
    return Response({"message": "Resource deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
