from django.contrib import admin
from .models import Language, DifficultyLevel, Tag, Resource

# Register your models here.

admin.site.register(Language)
admin.site.register(DifficultyLevel)
admin.site.register(Tag)
admin.site.register(Resource)