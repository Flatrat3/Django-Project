from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def weather_view(request):
    weather_data = {
        'city': 'Bakı',
        'temperature_c': 18,
        'temperature_f': 64.4,
        'description': 'Günəşli',
        'humidity': 55,
        'wind_kph': 12,
        'forecast': [
            {'day': 'Bazar ertəsi', 'min': 15, 'max': 19, 'desc': 'Buludlu'},
            {'day': 'Çərşənbə', 'min': 14, 'max': 21, 'desc': 'Günəşli'},
            {'day': 'Cümə', 'min': 13, 'max': 20, 'desc': 'Yağıntılı'},
        ]
    }
    return render (request, 'blog/weather.html', {'weather': weather_data})