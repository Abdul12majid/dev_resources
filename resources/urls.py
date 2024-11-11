from rest_framework.routers import DefaultRouter
from .views import LanguageViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'languages', LanguageViewSet)


urlpatterns = router.urls