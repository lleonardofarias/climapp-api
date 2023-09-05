import pytz
from django.http import JsonResponse
import requests
from datetime import datetime

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
        response_data = {
            "temperature": temperature,
            "city": city,
            "timestamp": timestamp
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Fail in obtain data"}, status=500)
