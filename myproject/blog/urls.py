from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('weather/', views.weather_view, name='weather'),
    path('add_musician/', views.add_musician, name='add_musician'),

]
