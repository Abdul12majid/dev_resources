from rest_framework.routers import DefaultRouter
from .views import LanguageViewSet, DifficultyLevelViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'difficulties', DifficultyLevelViewSet)


urlpatterns = router.urls