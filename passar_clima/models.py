from django.db import models

class WeatherData(models.Model):
    temperature = models.FloatField()
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"{self.city} - {self.timestamp}"

