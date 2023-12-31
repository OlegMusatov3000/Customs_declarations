from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
# Добавляем автоматическое формирование документации.
schema_view = get_schema_view(
    openapi.Info(
        title='customs_declarations',
        default_version='v1',
        description=(
            'Документация для приложения api проекта customs_declarations'
        ),
        contact=openapi.Contact(email='admin@admin.ru'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]