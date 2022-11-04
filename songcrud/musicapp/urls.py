from django.urls import path
from .views import index
from .views import ArtisteViewSet
from .views import SongViewSet
from .views import LyricViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', index, name='index')
]

router = DefaultRouter()
router.register(r'artistes', ArtisteViewSet, basename='artistes')
router.register(r'songs', SongViewSet, basename='songs')
router.register(r'lyrics', LyricViewSet, basename='lyrics')

urlpatterns = [] + router.urls