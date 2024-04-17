from django.contrib.sites import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseNotFound
import requests

from .forms import TaskForm
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(ListView):
    model = Task
    template_name = 'speedway_calendar/home.html'
    def get_queryset(self):
        return Task.objects.filter(author__username=self.request.user)

class TaskDetailsView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'speedway_calendar/task_details.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        place = task.place

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=153986837855671edcb6d89de1d74d34'

        try:
            response = requests.get(url.format(place))  # request the API data and convert the JSON to Python data types
            city_weather = response.json()
            celsius_temperature = round((((city_weather['main']['temp']) - 32) * 5/9), 1)

            weather = {
                'temperature': celsius_temperature,
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }

            context['weather'] = weather

            return context
        except:
            return {}
class addTaskView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'speedway_calendar/add_task.html'
    form_class = TaskForm
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


