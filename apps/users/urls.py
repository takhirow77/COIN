from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from apps.users.views import UserAPIViewsSet

router = DefaultRouter()
router.register('users', UserAPIViewsSet, basename='api_users')

urlpatterns = router.urls

    