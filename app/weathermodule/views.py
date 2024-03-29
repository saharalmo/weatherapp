from django.shortcuts import render 
from datetime import datetime as dt 
from django.conf import settings
from django.http.response import JsonResponse
from django.http import JsonResponse
import requests
from .models import weather 
def index(request):
    return render(request, 'weathermodule/index.html')

def trigger (request):
        city = request.GET.get("city") #send by user 
        weather_data =request_to_weatherapi(city)
        qset=weather.objects.filter(city__iexact=city)
        if qset.exists():
            qset.update(**weather_data)
            return JsonResponse({"data": [weather_data],"message":"Updated!"})
        else:
            weather.objects.create(**weather_data)
            return JsonResponse({"data": [weather_data],"message":"Created!"})
          
def request_to_weatherapi(city):
    URL = f"http://api.weatherapi.com/v1/current.json?key={settings.WA_APIKEY}&q={city}"
    res = requests.get(URL)
    res.raise_for_status()
    res_json = res.json()
    return{
        "city":res_json["location"]["name"],
        "description" : res_json["current"]["condition"]["text"],
        "icon":f'http:{res_json["current"]["condition"]["text"]}', 
        "temperature":res_json["current"]["temp_c"],
        "updated_date":dt.fromtimestamp(res_json["current"]["last_updated_epoch"]).strftime('%Y-%m-%d %H:%M:%S'),
        "api_response": res.text 
    }
    
    