from rest_framework import viewsets
from passar_clima.api.serializers import PassarClimaSerializer  
from passar_clima.models import WeatherData  

class PassarClimaViewSet(viewsets.ModelViewSet):
    serializer_class = PassarClimaSerializer  
    queryset = WeatherData.objects.all()  
