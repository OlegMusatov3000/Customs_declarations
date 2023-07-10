from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SignUpViewSet,
    AuthViewSet,
    GetEtgbViewSet,
)

router = DefaultRouter()

router.register('posting/global/etgb', GetEtgbViewSet, basename='etgb')

auth_urls = [
    path(
        'signup/',
        SignUpViewSet.as_view({'post': 'create'}),
        name='signup'
    ),
    path(
        'authdata/',
        AuthViewSet.as_view({'post': 'create'}),
        name='token'
    )
]

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('', include(router.urls)),
]
