from rest_framework.routers import DefaultRouter
from .views import LanguageViewSet, DifficultyLevelViewSet, TagViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'difficulties', DifficultyLevelViewSet)
router.register(r'tags', TagViewSet)


urlpatterns = router.urls