from . import views
from django.urls import path, include

app_name = "accounts"

# from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("logout/", views.LogoutView.as_view(), name="basic-logout"),
    path("login/", views.loginView.as_view(), name="basic-login"),
    path("signup/", views.SignupView.as_view(), name="basic-signup"),
    # djoser Token & JWT
    path("djsr/", include("djoser.urls.authtoken")),
    path("djsr/", include("djoser.urls.jwt")),
]
