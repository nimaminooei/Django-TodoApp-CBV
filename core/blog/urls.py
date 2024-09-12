from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path("",views.indexview.as_view(),name="index"),
    path("blog/",views.PostList.as_view(),name="list-post"),
    path("blog/post/create/", views.PostCreate.as_view(), name="create-post"),
    path("blog/post/detail/<int:pk>/", views.PostDetail.as_view(), name="detail-post"),
    path("blog/post/update/<int:pk>/", views.PostUpdate.as_view(), name="update-post"),
    path("blog/post/delete/<int:pk>/", views.PostDelete.as_view(), name="delete-post"),
    
]
