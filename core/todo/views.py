from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.core.cache import cache
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse_lazy
from django.http import JsonResponse
import requests

from .forms import TaskUpdateForm
from .models import Tasks


WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "4c6afb8de79979cf64c1e16c93bffa91"
CITY = "Tehran"
class WeatherAPIView(View):
    cache_key = 'weather_data'

    def get_weather_data(self):
        response = requests.get(WEATHER_API_URL, params={"q": CITY, "appid": API_KEY})
        return response.json()
    def get(self, request, *args, **kwargs):

        weather_data = cache.get(self.cache_key)

        if not weather_data:
            
            weather_data = self.get_weather_data()
            
            cache.set(self.cache_key, weather_data, timeout=20*60)

        return JsonResponse(weather_data)

class index(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = "tasks"
    template_name = "todo/task_list.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = ["task"]
    success_url = reverse_lazy("todo:index")
    context_object_name = "tasks"
    template_name = "todo/task_list.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = TaskUpdateForm
    template_name_suffix = "_update"
    success_url = reverse_lazy("todo:index")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Tasks
    success_url = reverse_lazy("todo:index")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskDone(LoginRequiredMixin, View):
    model = Tasks
    success_url = reverse_lazy("todo:index")

    def get(self, request, *args, **kwargs):
        Task = Tasks.objects.get(id=kwargs.get("pk"))
        Task.status = True
        Task.save()
        return redirect(self.success_url)


