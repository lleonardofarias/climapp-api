from django.urls import path, include
from rest_framework import routers
from passar_clima.api.viewsets import PassarClimaViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'passar_clima', PassarClimaViewSet, basename='weatherdata')

urlpatterns = [
    path('api/weather/', views.weather_api, name='weather_api'),
    path('', include(router.urls)),
]


