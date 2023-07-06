from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register('depoimentos', views.DepoimentosViewSet, basename='Depoimentos')

urlpatterns = [ 
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Para add imagens por meio do gerenciador de arquivos