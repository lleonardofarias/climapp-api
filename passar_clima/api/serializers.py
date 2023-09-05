from rest_framework import serializers
from passar_clima import models

class PassarClimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeatherData
        fields = '__all__'
