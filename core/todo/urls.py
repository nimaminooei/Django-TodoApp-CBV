from django.urls import path, include
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("create/", views.TaskCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.TaskUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.TaskDelete.as_view(), name="delete"),
    path("done/<int:pk>/", views.TaskDone.as_view(), name="done"),
    # API
    path("api/v1/", include("todo.api.v1.urls"), name="api"),
]
