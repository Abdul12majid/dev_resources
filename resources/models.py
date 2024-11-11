from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class DifficultyLevel(models.Model):
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.level


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
        

class Resource(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='resources')
    difficulty = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE, related_name='resources')
    tags = models.ManyToManyField(Tag, related_name='resources')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
