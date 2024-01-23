from django.contrib.sites import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
import requests


from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(ListView):
    model = Task
    template_name = 'speedway_calendar/home.html'

class TaskDetailsView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'speedway_calendar/task_details.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        place = task.place
        # print(Task.place)
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=153986837855671edcb6d89de1d74d34'


        city_weather = requests.get(url.format(place)).json()  # request the API data and convert the JSON to Python data types
        print(city_weather)
        celsius_temperature = round((((city_weather['main']['temp']) - 32) * 5/9), 1)

        weather = {
            'temperature': celsius_temperature,
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        context['weather'] = weather

        return context
