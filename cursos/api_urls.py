from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import CursoViewSet

router = DefaultRouter()
router.register('cursos', CursoViewSet, basename='api-curso')

urlpatterns = [
    path('token/', obtain_auth_token, name='api_token'),
    path('', include(router.urls)),
]