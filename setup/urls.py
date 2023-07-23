from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

#Configurações swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Jornada Milhas API",
      default_version='v1',
      description="Plataforma que reune destinos de viagens e reviews de viajantes",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jornada.urls')),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
