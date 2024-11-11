from rest_framework import serializers
from .models import Resource, Language, DifficultyLevel, Tag

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']

class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = ['id', 'level']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ResourceSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    difficulty = DifficultyLevelSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Resource
        fields = ['id', 'title', 'url', 'description', 'language', 'difficulty', 'tags', 'date_added']
