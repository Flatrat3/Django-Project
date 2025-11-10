import requests
from django.shortcuts import render
from .models import Post
import json


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def weather_view(request):
    # weather_data = {
    #     'city': 'Bakı',
    #     'temperature_c': 18,
    #     'temperature_f': 64.4,
    #     'description': 'Günəşli',
    #     'humidity': 55,
    #     'wind_kph': 12,
    #     'forecast': [
    #         {'day': 'Bazar ertəsi', 'min': 15, 'max': 19, 'desc': 'Buludlu'},
    #         {'day': 'Çərşənbə', 'min': 14, 'max': 21, 'desc': 'Günəşli'},
    #         {'day': 'Cümə', 'min': 13, 'max': 20, 'desc': 'Yağıntılı'},
    #     ]
    # }
    weather_data = None

    if request.method == "POST":
        city = request.POST.get('city')
        api_key = '05fd7f153cacf4e2711f7321f57b8860'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=az"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'Şəhər tapılmadı. Zəhmət olmasa düzgün ad daxil edin.'}


    return render(request, 'blog/weather.html', {'weather_data': weather_data})
