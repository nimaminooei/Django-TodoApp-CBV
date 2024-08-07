from django.urls import path

from .views import ApiTaskView, ApiTaskDetail

app_name = "api"

urlpatterns = [
    path("task/", ApiTaskView.as_view(), name="task_list"),
    path("task-detail/<int:id>/",ApiTaskDetail.as_view(),name="task_detail",),
]