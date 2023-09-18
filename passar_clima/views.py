import pytz
from django.http import JsonResponse
import requests
from datetime import datetime

def get_weather_icon(icon_code):   #use the openweather to get weather icons
    icon_url = f"http://openweathermap.org/img/w/{icon_code}.png"
    return icon_url

def weather_api(request):
    city = request.GET.get('city', '')
    unit = request.GET.get('unit')
    api_key = "your api key"
    base_url = "your weather api url"

    params = {
        "q": city,
        "appid": api_key,
        "units": unit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_info = response.json()
        temperature = weather_info['main']['temp']
        timestamp = datetime.now(pytz.timezone(request.GET.get('timezone', 'UTC'))).strftime('%H:%M:%S')
        current_weather = weather_info['weather'][0]['description']  
        icon_code = weather_info['weather'][0]['icon']  
        icon_url = get_weather_icon(icon_code)  
        
        response_data = {
            "temperature": temperature,
            "city": city,
            "timestamp": timestamp,
            "current_weather": current_weather,
            "icon_url": icon_url  
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Fail to obtain data"}, status=500)
