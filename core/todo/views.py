from django.shortcuts import redirect
from django.views.generic import View
from .models import Tasks
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskUpdateForm


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
