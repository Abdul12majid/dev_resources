from rest_framework.routers import DefaultRouter
from .views import LanguageViewSet, DifficultyLevelViewSet, TagViewSet, ResourceViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'difficulties', DifficultyLevelViewSet)
router.register(r'tags', TagViewSet)
router.register(r'resources', ResourceViewSet)


urlpatterns = router.urls